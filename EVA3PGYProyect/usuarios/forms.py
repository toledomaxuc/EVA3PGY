from django import forms
from .models import NuevoUsuario, Publicacion, Categoria
from django.db import models
from django.forms import ModelForm

  

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ('idUsuario',)
        fields = ["titulo","autor","contenido","categorias","imagen",]
        widgets = {
            'categorias': forms.TextInput(attrs={'type': 'hidden'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']