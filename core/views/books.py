from django_filters import views

from django.views import generic
from django.urls import reverse_lazy

from core import models
from core import forms
from core import filters


class Create(generic.CreateView):
    model = models.Book
    form_class = forms.Book
    template_name = 'core/books/edit.html'
    success_url = reverse_lazy('books_list')


class List(views.FilterView):
    model = models.Book
    filterset_class = filters.Book
    template_name = 'core/books/list.html'


class Update(generic.UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = 'core/books/edit.html'
    success_url = reverse_lazy('books_list')


class Delete(generic.DeleteView):
    model = models.Book
    template_name = 'core/books/delete.html'
    success_url = reverse_lazy('books_list')
