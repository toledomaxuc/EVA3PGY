#from django.conf.urls import url
from django.urls import path
from . import views
from .views import crear_publicacion



urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('POLITICA', views.POLITICA, name='POLITICA'),
    path('POPULAR', views.POPULAR, name='POPULAR'),
    path('DEPORTE', views.DEPORTE, name='DEPORTE'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('index/', views.cerrarSesion, name='cerrarSesion'),
    path('perfil/', views.iniciarSesion, name='iniciarSesion'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('publicacionPolitica/', views.publicacionPolitica, name='publicacionPolitica'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
]