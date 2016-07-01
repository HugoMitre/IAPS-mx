from django.conf.urls import patterns, url
from analysis import views
 
urlpatterns = [
    url(r'^$',   views.index,   name='index'),
]