from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docadmin/', include('docadmin.urls', namespace='docadmin')),
    path('', views.index, name="index"),
    path('api/', include('notes.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('logout/', views.logout),
]
