from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from core import routers

from core.views import authors
from core.views import books
from core.views import tags
from core.views import rest

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/index.html')),

    url(r'^api/', include(routers.router.urls)),
    url(r'^api/books/(?P<pk>\d+)/set_tag/$', rest.SetTag.as_view()),
    url(r'^api/books/(?P<pk>\d+)/revoke_tag/$', rest.RevokeTag.as_view()),

    url(r'^authors/$', authors.List.as_view(), name='authors_list'),
    url(r'^authors/create/$', authors.Create.as_view(), name='authors_create'),
    url(r'^authors/(?P<pk>\d+)/update/$', authors.Update.as_view(), name='authors_update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', authors.Delete.as_view(), name='authors_delete'),

    url(r'^tags/$', tags.List.as_view(), name='tags_list'),
    url(r'^tags/create/$', tags.Create.as_view(), name='tags_create'),
    url(r'^tags/(?P<pk>\d+)/update/$', tags.Update.as_view(), name='tags_update'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tags.Delete.as_view(), name='tags_delete'),

    url(r'^books/$', books.List.as_view(), name='books_list'),
    url(r'^books/create/$', books.Create.as_view(), name='books_create'),
    url(r'^books/(?P<pk>\d+)/update/$', books.Update.as_view(), name='books_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', books.Delete.as_view(), name='books_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
