from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your models here.
class NuevoUsuario(models.Model):
    
    idUsuario        = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)    
    telefono         = models.CharField(max_length=45)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    contrasena       = models.CharField(max_length=10, blank=True, null=True) 
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)


class Categoria(models.Model):
    idCategoria  = models.AutoField(primary_key=True, null=False)
    categoria    = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return str(self.categoria)
    
class Publicacion(models.Model):
    idPublicacion    = models.AutoField(primary_key=True)
    titulo           = models.CharField(max_length=255)
    autor            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones_autor')
    contenido        = models.TextField()
    categorias       = models.ManyToManyField(Categoria)
    imagen           = models.ImageField(upload_to='img/')
    idUsuario        = models.ForeignKey(User,on_delete=models.CASCADE)
    categoria        = models.ForeignKey('Categoria', on_delete=models.CASCADE,default=1, related_name='publicaciones')

    def __str__(self):
        return str(self.titulo)
    

