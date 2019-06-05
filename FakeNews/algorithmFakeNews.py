from DatabasePool import DatabasePool
from fakenews import fakenews
from myHtmlClass import myHtmlClass
from bson.objectid import ObjectId


def get_dimension(paramenter_url):
    try:
        f = fakenews()
        m = myHtmlClass()

        dimension_text = m.html_cleaner(paramenter_url)
        dimension_language = f.check_language(dimension_text)
        dimension_sentiment = f.check_sentiment(dimension_text)
        dimension_key_words = f.check_key_words(dimension_text)
        return dimension_language, dimension_sentiment, dimension_key_words
    except:
        return 0


def open_database():
    try:
        d = DatabasePool()
        c = d.connect_mongo()
    except:
        return 0
    return c


def language_score(url_id):
    global new_list
    x = data_collection.find({"url_id": url_id})
    nl = []
    for i in x:
        ll = i["language"]["documents"]
        new_list = [x["detectedLanguages"] for x in ll]
    nl.append([x["score"] for x in new_list[0]])
    return nl[0][0]


def sentiment_score(url_id):
    x = data_collection.find({"url_id": url_id})
    nl = []
    for i in x:
        ll = i["sentiment"]["documents"]
        nl = [x["score"] for x in ll]
    return nl[0]


def key_word_score(url_id):
    x = data_collection.find({"url_id": url_id})
    entityTypeScore = []
    wikipediaScore = []

    for i in x:
        ll = i["key_word"]["documents"]
        new_list = [x["entities"] for x in ll]

    lkeyword = new_list[0]
    for i in range(len(lkeyword)):
        l = lkeyword[i]
        lm = dict(l["matches"][0])

        try:
            wikipediaScore.append(lm["wikipediaScore"])
        except:
            entityTypeScore.append(lm["entityTypeScore"])

    return len(entityTypeScore), entityTypeScore, len(wikipediaScore), wikipediaScore


def log_classification(p_is_fake):
    if p_is_fake == 0:
        print("")
        print("Document is true")
        print("")
    else:
        print("")
        print("FAKE NEWS!!!")
        print("")


# Set fakenews object
f = fakenews()

# Set database
d = open_database()
database = d['fakenews']

#Documents to be analyzed
documents = [
    {"url": "https://noticias.uol.com.br/politica/ultimas-noticias/2019/06/04/lula-regime-semiaberto-procuradoria.htm", "is_fake": "0"},
    {"url": "https://esporte.uol.com.br/futebol/ultimas-noticias/2019/06/04/vice-da-cbf-aposta-que-neymar-pede-dispensa-tem-novo-video-vindo.htm", "is_fake": ""},
    {"url": "https://carros.uol.com.br/noticias/redacao/2019/06/04/bolsonaro-quer-fim-de-exame-de-drogas-e-multa-menor-por-rodar-sem-capacete.htm", "is_fake": "0"},
    {"url": "http://guiasaude.me/antiacne-aa9/", "is_fake": ""}
]
for doc in documents:
    url = doc["url"]
    print("")
    print(f"Working with url {url}")
    print("")

    v_is_fake = doc["is_fake"]

    # Define dictionary to be searched
    dict_url = {"url": url}

    # Set collections
    url_collection = database['url']
    data_collection = database['data_to_be_analyzed']

    # Reset variables
    vlanguage_score = 0.0
    vsentiment_score = 0.0

    d_url = url_collection.find(dict_url)
    if v_is_fake is not "":
        if url_collection.find(dict_url).count() > 0:
            return_is_fake = [x["is_fake"] for x in d_url]
            log_classification(int(return_is_fake[0]))
            continue
        else:
            # Insert url
            url_id = url_collection.insert_one(dict_url).inserted_id

            # Get dimensions
            language, sentiment, key_word = get_dimension(url)

            # Prepare data to be recorded
            dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}

            # Inserting data_collection
            data_to_be_analyzed_id = data_collection.insert_one(dict_data).inserted_id

            # Determine score values
            vlanguage_score = float(language_score(url_id))
            vsentiment_score = float(sentiment_score(url_id))
            total_entityTypeScore, entityTypeScore, total_wikipediaScore, wikipediaScore = key_word_score(url_id)

            sum_entityTypeScore = float(sum(entityTypeScore))
            avg_entityTypeScore = float(sum_entityTypeScore / total_entityTypeScore)

            sum_wikipediaScore = float(sum(wikipediaScore))
            avg_wikipediaScore = float(sum_wikipediaScore / total_wikipediaScore)

            url_collection.update_one({"url": url}, {"$set":
                                                         {"language_score": vlanguage_score,
                                                          "sentiment_score": vsentiment_score,
                                                          "total_entityTypeScore": total_entityTypeScore,
                                                          "total_wikipediaScore": total_wikipediaScore,
                                                          "avg_entityTypeScore": avg_entityTypeScore,
                                                          "avg_wikipediaScore": avg_wikipediaScore,
                                                          "is_fake": v_is_fake
                                                          }
                                                     })

            print(f"URL: {url} has been inserted.")
            print(f"URL id# is {url_id}.")
            print(f"Data id# is {data_to_be_analyzed_id}.")
            print("")
    elif url_collection.find(dict_url).count() > 0:
            return_is_fake = [x["is_fake"] for x in d_url]
            log_classification(int(return_is_fake[0]))
            continue
    else:
        url_swap_collection = database['url_swap']

        #Insert url_swap
        url_id = url_swap_collection.insert_one(dict_url).inserted_id

        #Get dimensions
        language, sentiment, key_word = get_dimension(url)

        #Prepare data to be recorded
        dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}

        #Insert data_collection_swap
        data_to_be_analyzed_id = data_collection.insert_one(dict_data).inserted_id

        #Determine score values
        vlanguage_score = float(language_score(url_id))
        vsentiment_score = float(sentiment_score(url_id))
        total_entityTypeScore, entityTypeScore, total_wikipediaScore, wikipediaScore = key_word_score(url_id)

        sum_entityTypeScore = float(sum(entityTypeScore))
        avg_entityTypeScore = float(sum_entityTypeScore / total_entityTypeScore)

        sum_wikipediaScore = float(sum(wikipediaScore))
        avg_wikipediaScore = float(sum_wikipediaScore / total_wikipediaScore)

        #Verify if the url is fake or not
        is_fake = f.classify_url([avg_entityTypeScore, avg_wikipediaScore, vlanguage_score, vsentiment_score, sum_entityTypeScore,sum_wikipediaScore])

        #Print classification of the url
        log_classification(int(is_fake[0]))

        #Remove swap registers
        url_swap_collection.delete_one({'_id': ObjectId(url_id)})
        data_collection.delete_one({'_id': ObjectId(data_to_be_analyzed_id)})

        #Inserting correct values
        url_id = url_collection.insert_one(dict_url).inserted_id
        url_collection.update_one({"url": url}, {"$set":
                                                    {"language_score": vlanguage_score,
                                                      "sentiment_score": vsentiment_score,
                                                      "total_entityTypeScore": total_entityTypeScore,
                                                      "total_wikipediaScore": total_wikipediaScore,
                                                      "avg_entityTypeScore": avg_entityTypeScore,
                                                      "avg_wikipediaScore": avg_wikipediaScore,
                                                      "is_fake": is_fake[0]
                                                    }
                                                 })

        # Inserting data collection
        dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}
        data_to_be_analyzed_id = data_collection.insert_one(dict_data).inserted_id
