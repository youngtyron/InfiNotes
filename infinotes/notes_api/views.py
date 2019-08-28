from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .serializers import ThemeSerializer
from .models import Theme
from .mongo_handler import NotesMongoHandler, MongoJSONEncoder
# from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.views import APIView

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def themes_list(request, format=None):
	user = User.objects.first()
	print(request.user)
	themes = Theme.objects.filter(user = request.user)
	serializer = ThemeSerializer(themes, many=True)
	data = JSONRenderer().render(serializer.data)
	return HttpResponse(data, content_type='json')


def notes_list(request, theme_id):
	user_id = 1
	notes = list(NotesMongoHandler.get_documents(user_id, theme_id))
	data = MongoJSONEncoder().encode(notes)
	return HttpResponse(data, content_type='json')
