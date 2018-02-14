from rest_framework import routers

from core.views import rest


router = routers.DefaultRouter()

router.register('books', rest.BookViewSet)
router.register('tags', rest.TagViewSet)
router.register('authors', rest.AuthorViewSet)
