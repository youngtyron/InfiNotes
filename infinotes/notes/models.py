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

class NoteManager(models.Manager):
    def all(self):
        return operations.get_all()

    def collection(self, table_name):
        queryset = operations.get_all_in_collection(table_name)
        noteSet = set()
        for q in queryset:
            note = Note(id=q['_id'],headline=q['headline'],subtheme=q['subtheme'],text=q['text'],footnote=q['footnote'],date=q['date'])
            noteSet.add(note)
        return noteSet

    def create(self, **kwargs):
        return operations.create_note(**kwargs)

class Note(djongomodels.Model):
	headline = djongomodels.CharField(max_length=50)
	subtheme = djongomodels.CharField(max_length=200)
	text = djongomodels.TextField()
	footnote = djongomodels.TextField()
	date = djongomodels.DateTimeField(auto_now_add=True)
	objects = NoteManager()

	class Meta:
		in_db = 'mongo'

	def __str__(self):
		return self.headline
