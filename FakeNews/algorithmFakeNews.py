from DatabasePool import DatabasePool
from fakenews import fakenews
from myHtmlClass import myHtmlClass

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


#List of urls to be analyzed
l_url = ["https://portal.horanoticia.com/tb12/ob/estimulante2/?src=outbrain&utm_source=outbrain&utm_medium=Casa+Vogue+-+Lazer+e+Cultura&utm_campaign=TBL14-ALL&utm_content=Estimulante+natural+ajuda+milhares+de+pessoas+e+esgota+no+Brasil.+Mas+&utm_term=Casa+Vogue+-+Lazer+e+Cultura&wt_token=afaa265e329f4a278246d3a7065fd76b&wt_campaign=008f53aa547f50767076f975ed421811c8&wt_ad=0002dc946a840e31eb75541d934676a8eb&wt_site=00c78b96442ada3338a091766f2e87bed0&wt_network=NativeAds"]

for url in l_url:

    f = fakenews()

    #Reset variables
    vlanguage_score = 0.0
    vsentiment_score = 0.0

    # Set database
    d = open_database()
    database = d['fakenews']

    # Set collection
    url_collection = database['url']

    #Define dictionary to be searched
    dict_url = {"url": url}
    d_url = url_collection.find(dict_url)

    if url_collection.find({"url": url}).count() == 0:
        url_id = url_collection.insert_one(dict_url).inserted_id
        print(f"Document url# {url_id} was inserted.")
    else:
        c = url_collection.find(dict_url)
        url_id = c[0]["_id"]

    #Set collection of data to be analyzed
    data_collection = database['data_to_be_analyzed']

    #Verify if the url was analyzed already
    if data_collection.find({"url_id": url_id}).count() == 0:
        language, sentiment, key_word = get_dimension(url)
        dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}
        data_collection.insert_one(dict_data)
        print(f"Document data_to_be_analyzed# with url# = {url_id} was inserted.")

        #Determine score values
        vlanguage_score = float(language_score(url_id))
        vsentiment_score = float(sentiment_score(url_id))
        key_word_score(url_id)
        total_entityTypeScore, entityTypeScore, total_wikipediaScore, wikipediaScore = key_word_score(url_id)

        sum_entityTypeScore = float(sum(entityTypeScore))
        avg_entityTypeScore = float(sum_entityTypeScore / total_entityTypeScore)

        sum_wikipediaScore = float(sum(wikipediaScore))
        avg_wikipediaScore = float(sum_wikipediaScore / total_wikipediaScore)

        url_collection.update_one({"url": url}, {"$set":
            {"language_score": vlanguage_score, "sentiment_score": vsentiment_score,
                 "total_entityTypeScore": total_entityTypeScore, "total_wikipediaScore": total_wikipediaScore,
                 "avg_entityTypeScore": avg_entityTypeScore, "avg_wikipediaScore": avg_wikipediaScore,
                 "is_fake": 1
            }
        })

        is_fake = f.classify_url([avg_entityTypeScore, avg_wikipediaScore, vlanguage_score, vsentiment_score, sum_entityTypeScore, sum_wikipediaScore])

        if is_fake == 0:
            print("Document is not Fake!")
        else:
            print("FAKE NEWS!!!")

    else:
        dfake = url_collection.find_one({"url": url})
        if int(dfake["is_fake"]) == 0:
            print("This document is not fake!")
        else:
            print("FAKE NEWS")

