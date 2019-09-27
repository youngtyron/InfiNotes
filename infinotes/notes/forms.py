from django.forms import ModelForm
from .models import Note

class NoteAdminForm(ModelForm):
    class Meta:
        model = Note
        fields = ['subtheme', 'text', 'footnote']
        # fields = ['headline', 'subtheme', 'text', 'footnote']
