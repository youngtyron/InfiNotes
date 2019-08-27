from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Theme(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	table_name = models.CharField(max_length=256, blank=True, null=True)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title