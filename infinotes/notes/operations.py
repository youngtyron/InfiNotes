from pymongo import MongoClient
from infinotes.settings import MONGO_DB


def insert_in_collection(obj):
	collection_name = "{}".format(obj.headline)
	client = MongoClient()
	db = client.MONGO_DB
	data = {'headline':obj.headline, 'subtheme': obj.subtheme, 'text': obj.text, 'footnote': obj.footnote, 'date':obj.date}
	db[collection_name].insert_one(data)
	return

def get_all_in_collection(collection_name):
	if collection_name in collection_names():
		client = MongoClient()
		db = client.MONGO_DB
		queryset = db[collection_name].find()
		return queryset

def collection_names():
	client = MongoClient()
	db = client.MONGO_DB
	return db.collection_names()
