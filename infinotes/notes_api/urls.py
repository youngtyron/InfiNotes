from django.urls import path
from django.conf.urls import url, include
from . import views
# from .views import ThemesView

urlpatterns = [
    path('themes/', views.themes_list),
    # path('themes/', ThemesView.as_view()),
    path('notes/<int:theme_id>/', views.notes_list),
]
