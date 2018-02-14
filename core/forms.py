from django import forms

from core import models


class Book(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = models.Tag.objects.filter(is_active=True)
