from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('themes/', views.themes_list),
    path('theme/<int:theme_id>/notes/', views.notes_list),
    path('theme/<int:theme_id>/create/', views.create_note),
]
