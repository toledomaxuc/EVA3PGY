#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('POLITICA', views.POLITICA, name='POLITICA'),
    path('POPULAR', views.POPULAR, name='POPULAR'),
    path('DEPORTE', views.DEPORTE, name='DEPORTE'),
    path('Formulario', views.Formulario, name='Formulario'),
]