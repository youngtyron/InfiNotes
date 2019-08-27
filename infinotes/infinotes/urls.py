from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from notes_api.mongo_main import MongoDatabase

#Переделать
try:
    MongoDatabase().connect()
except Exception as e:
    print("Error while connecting to MongoDB!")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', views.index, name="index"),
    path('api/', include('notes_api.urls'))
]
