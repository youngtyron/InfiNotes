from django.forms import ModelForm
from .models import Note

class NoteAdminForm(ModelForm):
    class Meta:
        model = Note
        fields = ['headline', 'subtheme', 'text', 'footnote']
