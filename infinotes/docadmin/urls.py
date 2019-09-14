from django.urls import path
from . import views
from .views import AddNoteFormView, DocAdminView, NotesListView

app_name = 'docadmin'

urlpatterns = [
    path('', DocAdminView.as_view(), name='index'),
    path('notelist/', NotesListView.as_view(), name='notelist'),
    path('addnote/', AddNoteFormView.as_view(), name='addnote'),
]
