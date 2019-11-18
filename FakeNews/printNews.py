import DatabasePool as db


### Creating database connection
dtb = db.DatabasePool()
c = dtb.connect_mongo()
database = c['fakenews']
url_collection = database['url']

c_url = url_collection.find({"is_fake": "1"})

for i in c_url:
    print(i["url"])
