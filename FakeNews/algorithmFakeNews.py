from DatabasePool import DatabasePool
from myHmlClass import myHtmlClass
from fakenews import fakenews
from bson.objectid import ObjectId
from pprint import pprint


def get_dimension():
    try:
        f = fakenews()
        m = myHtmlClass()
        text = m.hml_cleaner(url)
        dimension_language = f.check_language(url, text)
        dimension_sentiment = f.check_sentiment(url, text)
        dimension_key_words = f.check_key_words(url, text)
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
    x = data_collection.find({"url_id": url_id})
    for i in x:
        ll = i["language"]["documents"]
        new_list = [x["detectedLanguages"] for x in ll]
    nl = [x["score"] for x in new_list[0]]
    return float(nl[0])


def sentiment_score(url_id):
    x = data_collection.find({"url_id":url_id})
    for i in x:
        ll = i["sentiment"]["documents"]
        nl = [x["score"] for x in ll]
    return float(nl[0])

def key_word_score(url_id):
    x = data_collection.find({"url_id":url_id})
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
l_url = ["https://noticias.bol.uol.com.br/especiais/a-favela-pode-ter-tudo/index.htm"]

for url in l_url:

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

    if data_collection.find({"url_id": url_id}).count() == 0:
        language, sentiment, key_word = get_dimension()
        dict_data = {"url_id": url_id, "language": language, "sentiment": sentiment, "key_word": key_word}
        data_collection.insert_one(dict_data)
        print(f"Document data_to_be_analyzed# with url# = {url_id} was inserted.")

        #Determine score values
        language_score = float(language_score(url_id))
        sentiment_score = float(sentiment_score(url_id))
        key_word_score(url_id)
        total_entityTypeScore, entityTypeScore, total_wikipediaScore, wikipediaScore = key_word_score(url_id)

        sum_entityTypeScore = float(sum(entityTypeScore))
        avg_entityTypeScore = float(sum_entityTypeScore / total_entityTypeScore)

        sum_wikipediaScore = float(sum(wikipediaScore))
        avg_wikipediaScore = float(sum_wikipediaScore / total_wikipediaScore)

        url_collection.update_one({"url": url}, {"$set":
            {"language_score": language_score, "sentiment_score": sentiment_score,
                 "total_entityTypeScore": total_entityTypeScore, "total_wikipediaScore": total_wikipediaScore,
                 "avg_entityTypeScore": avg_entityTypeScore, "avg_wikipediaScore": avg_wikipediaScore,
                 "is_fake": 0
            }
        })
    else:
        dfake = url_collection.find_one({"url": url})
        if int(dfake["is_fake"]) == 0:
            print("This document is not fake!")
        else:
            print("This document is fake!")

