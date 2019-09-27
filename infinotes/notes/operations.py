import datetime
from pymongo import MongoClient
from infinotes.settings import MONGO_DB


def insert_in_collection(obj):
	collection_name = "{}".format(obj.headline)
	client = MongoClient()
	db = client.MONGO_DB
	data = {'headline':obj.headline, 'subtheme': obj.subtheme, 'text': obj.text, 'footnote': obj.footnote, 'date':obj.date}
	db[collection_name].insert_one(data)
	return

def get_all_in_collection(table_name):
	client = MongoClient()
	db = client.MONGO_DB
	queryset = db[table_name].find()
	return queryset

def create_note(**kwargs):
	client = MongoClient()
	db = client.MONGO_DB
	table_name = kwargs['table_name']
	subtheme = kwargs['subtheme']
	text = kwargs['text']
	footnote = kwargs['footnote']
	date = datetime.datetime.now()
	data = {'headline':table_name, 'subtheme': subtheme, 'text': text, 'footnote': footnote, 'date':date}
	resp = db[table_name].insert_one(data)
	return resp

def get_all():
	list = []
	client = MongoClient()
	db = client.MONGO_DB
	for collection in correct_collections():
		queryset = db[collection].find()
		list.append(queryset)
	return list


def collection_names():
	client = MongoClient()
	db = client.MONGO_DB
	return db.collection_names()

def correct_collections_fitler(x):
	return x == 'test_headline2'

def correct_collections():
	client = MongoClient()
	db = client.MONGO_DB
	collections = list(filter(correct_collections_fitler, db.collection_names()))
	return collections
