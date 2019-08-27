from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .serializers import ThemeSerializer
from .models import Theme
from .mongo import database, collection_name, documents, MongoJSONEncoder

# Create your views here.

def themes_list(request):
	user = User.objects.first()
	themes = Theme.objects.filter(user = user)
	serializer = ThemeSerializer(themes, many=True)
	data = JSONRenderer().render(serializer.data)
	return HttpResponse(data, content_type='json')

def notes_list(request, theme_id):
	user_id = 1
	notes = list(documents(user_id, theme_id))
	data = MongoJSONEncoder().encode(notes)
	return HttpResponse(data, content_type='json')
