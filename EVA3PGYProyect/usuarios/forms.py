from django import forms
from .models import NuevoUsuario

from django.forms import ModelForm

class usuarioForm(ModelForm):
    class Meta:
        model = NuevoUsuario
        fields = ("nombre",
                  "apellido_paterno",
                  "apellido_materno",
                  "email",
                  "fecha_nacimiento",
                  "telefono",
                  "direccion",
                  "contrasena")