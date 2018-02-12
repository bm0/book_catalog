from django.contrib import admin
from . import models


# Register your models here.

class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    inlines = (BookInline,)


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book)
admin.site.register(models.Tag)
