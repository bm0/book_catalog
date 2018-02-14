import django_filters

from django.db.models import Q

from core import models


class Book(django_filters.FilterSet):
    keyword = django_filters.CharFilter(label='Ключевое слово или фраза', method='filter_keyword')

    class Meta:
        model = models.Book
        fields = (
            'author', 'tags', 'pub_at', 'keyword'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tags'].queryset = models.Tag.objects.filter(is_active=True)
        self.filters['pub_at'].field.widget.attrs = {'class': 'datepicker'}

    def filter_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(author__first_name__icontains=value)
        )
