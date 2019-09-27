from django.urls import path
from . import views
from .views import AddNoteFormView, DocAdminView, NotesListView, ThemesListView, UserListView, UserDetailView, all_notes_list_view, add_note_form

app_name = 'docadmin'

urlpatterns = [
    path('', DocAdminView.as_view(), name='index'),
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='userdetail'),
    path('user/themes/<int:pk>/', ThemesListView.as_view(), name='themelist'),
    path('user/themes/<int:pk>/notes/', NotesListView.as_view(), name='notelist'),
    path('user/themes/<int:theme_id>/notes/add/', add_note_form, name='addnote'),
]
