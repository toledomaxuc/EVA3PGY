from django.contrib import admin
from .models import NuevoUsuario, Publicacion, Categoria

# Register your models here.
admin.site.register(NuevoUsuario)
admin.site.register(Publicacion)
admin.site.register(Categoria)