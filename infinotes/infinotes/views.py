from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

def index(request):
	return render(request, 'index.html')

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def logout(request, format=None):
	request.user.auth_token.delete()
	return HttpResponse(status=200)

# class DocAdminView()
