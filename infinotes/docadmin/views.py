from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from notes.models import Note
from notes.forms import NoteAdminForm


class DocAdminView(TemplateView):
    template_name = "docadmin.html"

class NotesListView(ListView):
    model = Note
    template_name = "notelist.html"


class AddNoteFormView(FormView):
    template_name = 'addnote.html'
    form_class = NoteAdminForm

    def get_success_url(self):
        return reverse('docadmin:notelist')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
