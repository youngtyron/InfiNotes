from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.urls import reverse
from notes.models import Theme, Note
from notes.forms import NoteAdminForm


class UserListView(ListView):
    model = User
    template_name = "userlist.html"

class UserDetailView(DetailView):
    model = User
    template_name = "userdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['themes_count'] = Theme.objects.filter(user = user).count()
        return context

class ThemesListView(ListView):
    model = Theme
    template_name = "themelist.html"

    def get_queryset(self):
        user = get_object_or_404(User, id = self.kwargs['pk'])
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.filter(user = user)
        elif self.model is not None:
            queryset = self.model._default_manager.filter(user = user)
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class DocAdminView(TemplateView):
    template_name = "docadmin.html"

class NotesListView(ListView):
    model = Note
    template_name = "notelist.html"

    def get_queryset(self):
        theme = get_object_or_404(Theme, id = self.kwargs['pk'])
        queryset = Note.objects.collection(table_name = theme.table_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme_id'] = self.kwargs['pk']
        return context

def all_notes_list_view(request):
    notes = Note.mongo_all()
    context = {'notes': notes}
    return render(request, 'notelist.html', context)

def add_note_form(request, theme_id):
    if request.method=='GET':
        form = NoteAdminForm()
        return render(request, 'addnote.html', {'form':form, 'theme_id': theme_id})
    elif request.method == 'POST':
        print(request.POST)
        theme_id = request.POST['theme_id']
        theme = get_object_or_404(Theme, id = theme_id)
        user_id = theme.user.id
        subtheme = request.POST['subtheme']
        text = request.POST['text']
        footnote = request.POST['footnote']
        table_name = "U{}T{}".format(user_id, theme_id)
        print(table_name)
        resp = Note.objects.create(table_name=table_name, subtheme=subtheme, text=text, footnote=footnote)
        print(resp)
        return redirect('docadmin:notelist', pk=theme_id)
        # form = NoteAdminForm()
        # return render(request, 'addnote.html', {'form':form, 'theme_id': theme_id})

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
