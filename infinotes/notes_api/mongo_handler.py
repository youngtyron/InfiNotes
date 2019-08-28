import json
from bson import ObjectId
from pymongo import MongoClient
from .mongo_main import MongoDatabase

class NotesMongoHandler(object):

    @staticmethod
    def database():
        db = MongoDatabase().connect()
        return db

    @classmethod
    def collection_name(self, user_id, theme_id):
        name = "notes_user_{}_theme_{}".format(user_id, theme_id)
        return name

    @classmethod
    def get_documents(self, user_id, theme_id):
        col_name = self.collection_name(user_id, theme_id)
        db = self.database()
        collection = db[col_name]
        documents = collection.find()
        return documents


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)