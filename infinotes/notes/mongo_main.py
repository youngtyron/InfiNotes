from pymongo import MongoClient
from infinotes.settings import MONGO_DB, MONGO_PORT, MONGO_HOST, MONGO_PASS, MONGO_USER


class MongoSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MongoSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MongoDatabase(metaclass=MongoSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            client = MongoClient(MONGO_HOST, MONGO_PORT)
            db = client[MONGO_DB]
            db.authenticate(MONGO_USER, MONGO_PASS)
            self.connection = db
        return self.connection
