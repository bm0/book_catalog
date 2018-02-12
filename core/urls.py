from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import author
from .views import tags

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/base.html') ),

    url(r'^authors/$', author.List.as_view(), name='authors_list'),
    url(r'^authors/create/$', author.Create.as_view(), name='authors_create'),
    url(r'^authors/(?P<pk>\d+)/update/$', author.Update.as_view(), name='authors_update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', author.Delete.as_view(), name='authors_delete'),

    url(r'^tags/$', tags.List.as_view(), name='authors_list'),
    url(r'^tags/create/$', tags.Create.as_view(), name='tags_create'),
    url(r'^tags/(?P<pk>\d+)/update/$', tags.Update.as_view(), name='tags_update'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tags.Delete.as_view(), name='tags_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)