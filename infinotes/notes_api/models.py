from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongomodels
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)
# from djongo.models import forms as djongoforms

# Create your models here.
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

	def __str__(self):
		return self.headline

	def create(self, headline, subtheme, text, footnote):
		pass

	class Meta:
		in_db = 'mongo'
