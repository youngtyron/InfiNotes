from django.db import models
from django.contrib.auth.models import User
from django.http import QueryDict
from djongo import models as djongomodels
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)
from . import operations


class Theme(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	table_name = models.CharField(max_length=256, blank=True, null=True)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title


class Note(djongomodels.Model):
	headline = djongomodels.CharField(max_length=50)
	subtheme = djongomodels.CharField(max_length=200)
	text = djongomodels.TextField()
	footnote = djongomodels.TextField()
	date = djongomodels.DateField(auto_now_add=True)
	objects = djongomodels.DjongoManager()

	class Meta:
		in_db = 'mongo'

	def __str__(self):
		return self.headline

	def __init__(self, *args, **kwargs):
		self.headline = kwargs['headline']
		self.subtheme = kwargs['subtheme']
		self.text = kwargs['text']
		self.footnote = kwargs['footnote']
		self.date = kwargs['date']
		return

	def save(self, *args, **kwargs):
		operations.insert_in_collection(self)
		return self

	@classmethod
	def all(cls, collection):
		raw_queryset = operations.get_all_in_collection(collection)
		list = []
		for q in raw_queryset:
			note = Note(headline=q['headline'], subtheme=q['subtheme'], text=q['text'],footnote=q['footnote'],date=q['date'])
			list.append(note)
		return list
