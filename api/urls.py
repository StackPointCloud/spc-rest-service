from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('api.views',
    url(r'^architectures/$', 'architecture_list'),
    url(r'^architectures/(?P<pk>[0-9]+)/$', 'architecture_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)