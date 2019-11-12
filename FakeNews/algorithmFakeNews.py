from DatabasePool import DatabasePool
from fakenews import fakenews
from myHtmlClass import myHtmlClass
from bson.objectid import ObjectId
import json

def get_dimension(paramenter_url):
    try:
        f = fakenews()
        m = myHtmlClass()

        dimension_text = m.prepare_text(paramenter_url)
        dimension_text = dimension_text[:5120]
        # print(f"--->{dimension_text}<---")
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
    #print("url_id ---->", url_id)
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
        print("Document is true")
        print("***"*30)
        print("")
        print("")
    else:
        print("FAKE NEWS!!!")
        print("***"*30)
        print("")
        print("")


# Set fakenews objectx
f = fakenews()

# Set database
d = open_database()
database = d['fakenews']

#Documents to be analyzed
# if you need to training a text, inform is_fake parameter with the knowledge value
# if you need to classify the text, pass is_fake parameter with blank value
# 0 = not fake
# 1 = is fake

#documents = [
#    {"url": "https://noticia-tv.com/entrevista-helen-sbt/?utm_source=taboola&utm_medium=PHYTO-2B-DESK-CP1&utm_campaign=editoraabril-exame", "is_fake":"1"},
#]


json_file = open("/Users/arnaldo.pedroso/git/Monografia/news.json", "r", encoding="utf-8")

news = json.load(json_file)

for doc in news:
    url = doc["url"]
    print("==*"*30)
    print(f"Working with url {url}")
    print("==*"*30)

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
        if url_collection.count_documents(dict_url) >0:
            try:
                return_is_fake = [x["is_fake"] for x in d_url]
            except:
                print("Error - ignoring this url")
                url_collection.delete_one({"url": url})
                continue

            log_classification(int(return_is_fake[0]))
            continue
        else:
            # Insert url
            url_id = url_collection.insert_one(dict_url).inserted_id

            # Get dimensions

            try:
                language, sentiment, key_word = get_dimension(url)
            except:
                url_collection.delete_one({"url": url})
                continue


            # Prepare data to be recorded
            dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}

            # Inserting data_collection
            data_to_be_analyzed_id = data_collection.insert_one(dict_data).inserted_id

            # Determine score values
            vlanguage_score = float(language_score(url_id))
            vsentiment_score = float(sentiment_score(url_id))
            total_entityTypeScore, entityTypeScore, total_wikipediaScore, wikipediaScore = key_word_score(url_id)

            sum_entityTypeScore = float(sum(entityTypeScore))

            try:
                avg_entityTypeScore = float(sum_entityTypeScore / total_entityTypeScore)
            except ZeroDivisionError:
                avg_entityTypeScore = 0

            sum_wikipediaScore = float(sum(wikipediaScore))

            try:
                avg_wikipediaScore = float(sum_wikipediaScore / total_wikipediaScore)
            except ZeroDivisionError:
                avg_wikipediaScore = 0

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
            print("--"*30)
    elif url_collection.count_documents(dict_url) > 0:
            try:
                return_is_fake = [x["is_fake"] for x in d_url]
            except:
                print("Error - ignoring this url")
                url_collection.delete_one({"url": url})
                continue
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
        is_fake = f.classify_url([avg_entityTypeScore, avg_wikipediaScore, vlanguage_score, vsentiment_score, sum_entityTypeScore, sum_wikipediaScore])

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
#Finish
exit(1)
