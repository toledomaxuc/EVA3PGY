from django import forms
from .models import NuevoUsuario
<<<<<<< HEAD

=======
from .models import Noticia
>>>>>>> origin/MAX3
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
<<<<<<< HEAD
                  "contrasena")
=======
                  "contrasena")
        

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen']        
>>>>>>> origin/MAX3
