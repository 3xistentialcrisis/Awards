from django.urls import url, include
from . import views

app_name = 'ourawards'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'signup/', views.signup, name='signup'),
    url(r'account/', include('django.contrib.auth.urls')),
]