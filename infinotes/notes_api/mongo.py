from pymongo import MongoClient

import json
from bson import ObjectId

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "my_documents_base"
MONGO_USER = "my_documents_user"
MONGO_PASS = "my_documents_password"

# class ThemeHandler(object):

def database():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DB]
    db.authenticate(MONGO_USER, MONGO_PASS)
    return db

def collection_name(user_id, theme_id):
    name = "notes_user_{}_theme_{}".format(user_id, theme_id)
    return name

def documents(user_id, theme_id):
    col_name = collection_name(user_id, theme_id)
    db = database()
    collection = db[col_name]
    documents = collection.find()
    return documents


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
