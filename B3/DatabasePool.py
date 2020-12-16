from pymongo import MongoClient

class DatabasePool():
    """Class created to optmize connection with database"""

    def __init__(self, host_name="localhost", port="27017"):
        self.host_name = host_name
        self.port = port

    def connect_mongo(self):
        return MongoClient(self.host_name, self.port)
