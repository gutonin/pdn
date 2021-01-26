from django.conf.urls import url, include 
from artigos import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<categoria>[\w-]+)\/(?P<artigo>[\w-]+)\/$', views.materia,name='materia'),
    url(r'^(?P<categoria>[\w-]+)\/$', views.categoria,name='categoria'),
]