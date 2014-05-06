from django.conf.urls import patterns, url, include
from rest_framework import routers
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'architecture', views.ArchitectureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^architectures/$', views.ArchitectureList.as_view()),
	url(r'^architectures/(?P<pk>[0-9]+)/$', views.ArchitectureDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)