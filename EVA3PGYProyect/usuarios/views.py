from django.shortcuts import render

# Create your views here.

def index(request):
    context={} 
    return render(request, 'usuarios/index.html', context)

def registro(request):
    context={} 
    return render(request, 'usuarios/registro.html', context)

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

