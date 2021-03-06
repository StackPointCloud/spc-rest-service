from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
	url(r'^architecture/$', views.ArchitectureList.as_view()),
	url(r'^architecture/(?P<pk>[0-9]+)/$', views.ArchitectureDetail.as_view()),
	)

urlpatterns = format_suffix_patterns(urlpatterns)