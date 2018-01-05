import pymongo


class Database(object):
    URI = "mongodb://haris:haris123@ds239587.mlab.com:39587/heroku_vm734g3w"
    DATABASE = None

    @staticmethod
    def initalisation():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, updated):
        Database.DATABASE[collection].find_one_and_update(query, updated)
