from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from .models import Note


class AboutPageTemplateView(TemplateView):
    """
    A class-based view that renders the home page.
    """
    template_name = 'notebook_app/about.html'
    extra_context = {'page_title': 'About - Notebook'}


class NotesListView(ListView):
    model = Note
    template_name = 'notebook_app/home.html'
    context_object_name = 'notes'
    extra_context = {'page_title': 'Notebook'}
    ordering = ['-date_added']


class NotesDetailView(DetailView):
    model = Note
    template_name = 'notebook_app/note_detail.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super(NotesDetailView, self).get_context_data()
        context['page_title'] = self.object.title + ' - Notebook'
        return context


class NotesCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notebook_app/note_create_update.html'
    extra_context = {'page_title': 'Create Note - Notebook',
                     'button_text': 'Create',
                     'page_header': 'Create a new note'}


class NotesUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notebook_app/note_create_update.html'

    def get_context_data(self, **kwargs):
        context = super(NotesUpdateView, self).get_context_data()
        context['button_text'] = 'Update'
        context['page_header'] = 'Update note'
        context['page_title'] = 'Update - ' + self.object.title[:15] + ' - Notebook'
        return context


class NotesDeleteView(DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notebook-home')

    def get_context_data(self, **kwargs):
        context = super(NotesDeleteView, self).get_context_data()
        context['page_title'] = 'Confirm - ' + self.object.title[:15] + ' - Notebook'
        return context

