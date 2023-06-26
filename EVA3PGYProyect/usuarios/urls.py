#from django.conf.urls import url
from django.urls import path
from . import views
from .views import BuscarNoticias


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('POLITICA', views.PoliticaView.as_view(), name='POLITICA'),
    path('POPULAR', views.PopularView.as_view(), name='POPULAR'),
    path('DEPORTE', views.DeporteView.as_view(), name='DEPORTE'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('index/', views.cerrarSesion, name='cerrarSesion'),
    path('perfil/', views.iniciarSesion, name='iniciarSesion'),
    path('categoria', views.categoria, name='categoria'),
    path('resultados-busqueda/', views.buscar, name='resultados_busqueda'),
    path('ingresar-noticia/', views.ingresar_noticia, name='ingresar_noticia'),
    path('editar-noticia/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('periodista', views.periodista, name='periodista')
]