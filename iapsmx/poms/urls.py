from django.conf.urls import patterns, url
from poms import views
 
urlpatterns = [
    url(r'^$',   views.index,   name='index'),
]