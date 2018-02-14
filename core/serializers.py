from rest_framework import serializers

from core import models


class Book(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = models.Book
        fields = '__all__'


class Tag(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class Author(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class SetTag(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
        read_only_fields = (
            'name',
            'description',
            'preview',
            'author'
        )
        extra_kwargs = {
            'tags': {
                'queryset': models.Tag.objects.filter(is_active=True)
            }
        }


class RevokeTag(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
        read_only_fields = (
            'name',
            'description',
            'preview',
            'author'
        )

    def update(self, instance, validated_data):
        instance.tags.remove(*validated_data['tags'])

        return instance
