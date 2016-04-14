from django.conf.urls import url
from personas import views
 
urlpatterns = [
    url(r'^$',   views.index,   name='index'),
]