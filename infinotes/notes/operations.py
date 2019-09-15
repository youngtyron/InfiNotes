from pymongo import MongoClient
from infinotes.settings import MONGO_DB


def insert_in_collection(obj):
	collection_name = "{}".format(obj.headline)
	client = MongoClient()
	db = client.MONGO_DB
	data = {'headline':obj.headline, 'subtheme': obj.subtheme, 'text': obj.text, 'footnote': obj.footnote, 'date':obj.date}
	db[collection_name].insert_one(data)
	return
