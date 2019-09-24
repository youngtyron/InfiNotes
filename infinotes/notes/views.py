import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .serializers import ThemeSerializer
from .models import Theme, Note
from .mongo_handler import NotesMongoHandler, MongoJSONEncoder
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET'])
@permission_classes((AllowAny,))
def test_dev_func(request, format=None):
	all = Note.all('test_headline2')
	return HttpResponse({'foo':'bar'}, content_type='json')

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def themes_list(request, format=None):
	user = request.user
	themes = Theme.objects.filter(user = request.user)
	serializer = ThemeSerializer(themes, many=True)
	data = JSONRenderer().render(serializer.data)
	return HttpResponse(data, content_type='json')

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def notes_list(request, theme_id, format=None):
	user = request.user
	theme = Theme.objects.get(id = theme_id)
	if theme.user == user:
		notes = list(NotesMongoHandler.get_documents(user.id, theme_id))
		data = MongoJSONEncoder().encode(notes)
		return HttpResponse(data, content_type='json')
	else:
		return HttpResponse(status=400)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_note(request, theme_id, format=None):
	user = request.user
	theme = Theme.objects.get(id = theme_id)
	if theme.user == user:
		data = json.loads(request.body.decode('utf-8'))
		subtheme = data['subtheme']
		text = data['text']
		footnote = data['footnote']
		new_note = NotesMongoHandler.create_document(user.id, theme_id, subtheme, text, footnote)
		data = MongoJSONEncoder().encode(new_note)
		return HttpResponse(data, content_type='json')
	else:
		return HttpResponse(status=400)
