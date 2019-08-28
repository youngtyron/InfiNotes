from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from notes_api.mongo_main import MongoDatabase

#Переделать
# try:
#     MongoDatabase().connect()
# except Exception as e:
#     print("Error while connecting to MongoDB!")

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/login/', jwt_views.obtain_jwt_token),
    path('', views.index, name="index"),
    path('api/', include('notes_api.urls')),
    path('api-token-auth/', obtain_auth_token),
]
