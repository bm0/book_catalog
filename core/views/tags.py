from django_filters import views

from django.views import generic
from django.urls import reverse_lazy

from core import models


class Create(generic.CreateView):
    model = models.Tag
    fields = '__all__'
    template_name = 'core/tags/edit.html'
    success_url = reverse_lazy('tags_list')


class List(views.FilterView):
    model = models.Tag
    template_name = 'core/tags/list.html'

    def get_context_data(self, **kwargs):
        kwargs['colors'] = (
            'pink lighten-1',
            'indigo', 'blue',
            'cyan','amber',
            'orange'
        )

        return super().get_context_data(**kwargs)


class Update(generic.UpdateView):
    model = models.Tag
    fields = '__all__'
    template_name = 'core/tags/edit.html'
    success_url = reverse_lazy('tags_list')


class Delete(generic.DeleteView):
    model = models.Tag
    template_name = 'core/tags/delete.html'
    success_url = reverse_lazy('tags_list')
