from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import NuevoUsuario
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from .models import Noticia
from django.db.models import Q
from django.views.generic import TemplateView
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context={} 
    return render(request, 'usuarios/index.html', context)

#Funcion de registro
def registro(request):
    if request.method == 'GET':
        #si el metodo es GET, vuelve a registro.html y muestra el formulario
        return render(request, 'usuarios/registro.html', {
            'form': UserCreationForm
        })
    else:
        #Si el metodo es POST, valida ambas contraseñas que sean iguales para pasar a
        #guardar el objeto completo
        if request.POST['password1'] == request.POST['password2']:
            try:          
                nombre           = request.POST["nombre"]
                aPaterno         = request.POST["paterno"]
                aMaterno         = request.POST["materno"]
                email            = request.POST["email"]
                fechaNac         = request.POST["fechaNac"]
                telefono         = request.POST["telefono"]
                direccion        = request.POST["direccion"]
                contrasena       = request.POST["password1"]
                activo           = '1'
                #en cada variable, luego en la variable objeto guarda todo juntito
                    
                objeto = NuevoUsuario.objects.create(
                                            nombre=nombre,
                                            apellido_paterno=aPaterno,
                                            apellido_materno=aMaterno,
                                            email=email,
                                            fecha_nacimiento=fechaNac,
                                            telefono=telefono,
                                            direccion=direccion,
                                            contrasena=contrasena,                                  
                                            activo=1)
                #lo tira a la base de datos con .save()
                objeto.save()
                login(request, objeto)
                #y vuelve a registro.html donde muestra el "error" de usuario creado
                return render (request, 'usuarios/registro.html',{
                    'form': UserCreationForm,
                    "error": 'usuario creado'
                })
            except IntegrityError:
                return render (request, 'usuarios/registro.html',{
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
    return render (request, 'usuarios/registro.html',{
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
                })

def cerrarSesion(request):
    #cierre de sesion con import logout
    logout(request)
    return redirect(index)

def iniciarSesion(request): 
    #inicio de sesion con metodo post, donde solicita username(correo) y password
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('contrasena')

        #se autentica que los valores correspondan a los de la BD y se pasa a la variable "user"
        user = authenticate(request, username=username, password=password)
        print("login exitoso")
        #si el usuario esta vacio, solicita neuvamente el usuario
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            error_message = "Credenciales inválidas. Inténtalo de nuevo."
    else:
        error_message = None

    return render(request, 'usuarios/perfil.html', {
        'error_message': error_message,
    })

class PoliticaView(TemplateView):
    template_name = 'usuarios/POLITICA.html'

class PopularView(TemplateView):
    template_name = 'usuarios/POPULAR.html'

class DeporteView(TemplateView):
    template_name = 'usuarios/DEPORTE.html'

def Formulario(request):
    context={} 
    return render(request, 'usuarios/Formulario.html' , context)

def categoria(request):
    context={} 
    return render(request, 'usuarios/categoria.html' , context)

def periodista(request):
    context={} 
    return render(request, 'usuarios/periodista.html', context)


class PoliticaView(TemplateView):
    template_name = 'usuarios/POLITICA.html'

class PopularView(TemplateView):
    template_name = 'usuarios/POPULAR.html'

class DeporteView(TemplateView):
    template_name = 'usuarios/DEPORTE.html'

class BuscarNoticias(ListView):
    model = Noticia
    template_name = 'usuarios/resultados_busqueda.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(periodista__icontains=query) |
                Q(categoria__icontains=query) |
                Q(palabra_clave__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        return context


def buscar(request):
    query = request.GET.get('query')
    query_lower = query.lower()

    if query_lower == 'deporte':
        return redirect('DEPORTE')
    elif query_lower == 'politica':
        return redirect('POLITICA')
    elif query_lower == 'popular':
        return redirect('POPULAR')
    elif query_lower == 'maria' or query_lower == 'maria plaza':
        return redirect('POPULAR')
    elif query_lower == 'isabel' or query_lower == 'isabel caro':
        return redirect('POLITICA')
    elif query_lower == 'cesar' or query_lower == 'cesar vasquez':
        return redirect('DEPORTE')
    else:
        resultados = Noticia.objects.filter(
            Q(periodista__icontains=query) |
            Q(categoria__icontains=query) |
            Q(palabra_clave__icontains=query)
        )
        return render(request, 'usuarios/resultados_busqueda.html', {'resultados': resultados, 'query': query})
    

#CRUD
# 
def ingresar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoticiaForm()
    
    context = {'form': form}
    return render(request, 'usuarios/ingresar_noticia.html', context)

def editar_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoticiaForm(instance=noticia)
    
    context = {'form': form}
    return render(request, 'usuarios/editar_noticia.html', context)    


@login_required
def perfil(request):
    # Obtener los datos del usuario
    usuario = request.user

    # Pasar los datos del usuario al contexto
    context = {
        'nombre': usuario.first_name,
        'apellido': usuario.last_name,
        'email': usuario.email
    }

    return render(request, 'usuarios/perfil.html', context)

