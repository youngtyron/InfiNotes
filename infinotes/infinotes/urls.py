from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('api/', include('notes_api.urls')),
    path('api-token-auth/', obtain_auth_token),
]
