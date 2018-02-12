from django_filters import views

from django.views import generic
from django.urls import reverse_lazy

from .. import models


class Create(generic.CreateView):
    model = models.Author
    fields = '__all__'
    template_name = 'core/authors/edit.html'
    success_url = reverse_lazy('authors_list')


class List(views.FilterView):
    model = models.Author
    filter_fields = ('first_name', 'last_name', 'email',)
    template_name = 'core/authors/list.html'


class Update(generic.UpdateView):
    model = models.Author
    fields = '__all__'
    template_name = 'core/authors/edit.html'
    success_url = reverse_lazy('authors_list')


class Delete(generic.DeleteView):
    model = models.Author
    template_name = 'core/authors/delete.html'
    success_url = reverse_lazy('authors_list')
