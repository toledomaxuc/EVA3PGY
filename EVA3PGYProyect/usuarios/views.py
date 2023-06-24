from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import NuevoUsuario, Publicacion, Categoria
from django.contrib.auth import login, logout, authenticate
from .forms import PublicacionForm, CategoriaForm
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
                objeto.save()
                login(request, objeto)            
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
    logout(request)
    return redirect(index)

def iniciarSesion(request): 
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('contrasena')

        user = authenticate(request, username=username, password=password)
        print("login exitoso")
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


def publicacion(request):
    context = {}
    if request.user.is_authenticated:
        context["username"] = request.user.username
    categorias = Categoria.objects.all()
    context["categorias"] = categorias
    estado = Publicacion.objects.filter(idUsuario=request.user)
    context["publicaciones"] = estado
    publicacion = Publicacion.objects.all()
    return render(request, 'usuarios/POPULAR.html', {'publicaciones' : publicacion})

def publicacionPolitica(request):
    context = {}
    if request.user.is_authenticated:
        context["username"] = request.user.username
    categorias = Categoria.objects.all()
    context["categorias"] = categorias
    estado = Publicacion.objects.filter(idUsuario=request.user)
    context["publicaciones"] = estado
    publicacion = Publicacion.objects.all()
    return render(request, 'usuarios/POLITICA.html', {'publicaciones' : publicacion})

@login_required
def crear_publicacion(request):
    context = {}
    if request.user.is_authenticated:
        context["username"] = request.user.username
        if request.method == "POST":
            estado = Categoria.objects.get(idCategoria='1')
            form = PublicacionForm(request.POST, request.FILES)
            categoria_form = CategoriaForm(request.POST)
            if form.is_valid() and categoria_form.is_valid():
                publicacion = form.save(commit=False)
                publicacion.idUsuario = request.user
                publicacion.save()

                categoria = categoria_form.cleaned_data['categoria']
                publicacion.categorias.add(categoria)
                return redirect('publicacion')
            else:
                print(form.errors)
                print(categoria_form.errors)
        else:
            form = PublicacionForm()
            categoria_form = CategoriaForm()
        context["formulario"] = form
        context["categoria_formulario"] = categoria_form
    return render(request, "usuarios/agregar.html", {
        'formPub' : PublicacionForm
    })

def crear_categoria(request):
    context = {}
    if request.user.is_authenticated:
        context["username"] = request.user.username
        if request.method == "POST":
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(publicacion)
            else:
                print(form.errors)
        else:
            form = CategoriaForm()
        context["form"] = form
    return render(request, "usuarios/agregar_categoria.html", context)


@login_required
def editPublicacion(request, idPublicacion):
    return redirect(publicacion)




def POLITICA(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'usuarios/POLITICA.html', {'publicaciones' : publicacion})

def POPULAR(request):
    
    publicacion = Publicacion.objects.all()
    return render(request, 'usuarios/POPULAR.html', {'publicaciones' : publicacion})

def DEPORTE(request):
    context={} 
    return render(request, 'usuarios/DEPORTE.html', context)

def Formulario(request):
    context={} 
    return render(request, 'usuarios/Formulario.html' , context)

def categoria(request):
    context={} 
    return render(request, 'usuarios/agregar.html' , context)


    


