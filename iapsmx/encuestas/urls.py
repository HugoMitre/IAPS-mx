from django.conf.urls import patterns, url
from encuestas import views
 
urlpatterns = [
    url(r'^(?P<pk>\d+)/dimensional$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/discreta/(?P<encuesta_id>\d+)$',views.encuesta_discreta, name='encuesta_discreta'),
    url(r'^instrucciones$', views.instrucciones, name='instrucciones'),
]