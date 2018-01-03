import pymongo
class Database(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None

    @staticmethod
    def initalisation():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['assignment']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)