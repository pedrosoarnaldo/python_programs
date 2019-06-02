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

#Url to be analyzed
url = "https://g1.globo.com/politica/noticia/2019/06/01/bolsonaro-diz-que-quer-manter-estados-e-municipios-na-reforma-da-previdencia.ghtml"

#Set database
d = open_database()
database = d['fakenews']

#Set collection
url_collection = database['url']

#Define dictionary to be searched
dict_url = {"url": url}
d_url = url_collection.find(dict_url)

if len(dict(d_url)) == 0:
    url_id = url_collection.insert_one(dict_url).inserted_id
    print(url_id)
else:
    c = url_collection.find(dict_url)
    url_id = c[0]["_id"]

#Set collection of data to be analyzed
data_collection = database['data_to_be_analyzed']

if data_collection.find({"url_id":url_id}).count() == 0:
    language, sentiment, key_word = get_dimension()
    dict_data = {"url_id": url_id, "language":language, "sentiment":sentiment, "key_word":key_word}
    data_collection.insert_one(dict_data).inserted_id