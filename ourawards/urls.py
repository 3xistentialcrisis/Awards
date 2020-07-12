from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('users', views.UserViewSet)

app_name = 'ourawards'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'signup/', views.signup, name='signup'),
    url(r'account/', include('django.contrib.auth.urls')),
    url(r'api/', include(router.urls)),
    url(r'(?P<username>.+)/profile/$', views.user_profile, name='userprofile'),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'profile/(?P<username>.+)/$', views.profile, name='profile'),
    url(r'profile/(?P<username>/settings.+)/$', views.edit_profile, name='edit'),
    url(r'project/(?<post>.+)/$', views.project, name='project')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)