from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('themes/', views.themes_list),
    path('notes/<int:theme_id>/', views.notes_list),
]
