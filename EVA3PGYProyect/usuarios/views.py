from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import NuevoUsuario
from django.contrib.auth import login, logout, authenticate

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

def POLITICA(request):
    context={} 
    return render(request, 'usuarios/POLITICA.html', context)

def POPULAR(request):
    context={} 
    return render(request, 'usuarios/POPULAR.html' , context)

def DEPORTE(request):
    context={} 
    return render(request, 'usuarios/DEPORTE.html', context)

def Formulario(request):
    context={} 
    return render(request, 'usuarios/Formulario.html' , context)

def categoria(request):
    context={} 
    return render(request, 'usuarios/categoria.html' , context)

