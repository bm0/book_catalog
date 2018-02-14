from rest_framework import generics
from rest_framework import viewsets

from core import serializers
from core import models


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Book
    queryset = models.Book.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Tag
    queryset = models.Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Author
    queryset = models.Book.objects.all()


class SetTag(generics.UpdateAPIView):
    serializer_class = serializers.SetTag
    queryset = models.Book.objects.all()


class RevokeTag(generics.UpdateAPIView):
    serializer_class = serializers.RevokeTag
    queryset = models.Book.objects.all()
