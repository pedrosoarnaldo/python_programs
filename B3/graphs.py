import DatabasePool


def setdb():
    try:
        mongo = DatabasePool.DatabasePool()
        return mongo.connect_mongo()
    except:
        print('Error connecting to mongodb')


c = setdb()
c.close()

