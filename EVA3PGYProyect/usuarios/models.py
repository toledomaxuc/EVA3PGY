from django.db import models

# Create your models here.
class NuevoUsuario(models.Model):
    
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
    

#buscador

class Noticia(models.Model):
    PERIODISTA_CHOICES = (
        ('Maria Plaza', 'Maria Plaza'),
        ('Isabel Caro', 'Isabel Caro'),
        ('Cesar Vasquez', 'Cesar Vasquez'),
    )

    CATEGORIA_CHOICES = (
        ('POPULAR', 'POPULAR'),
        ('POLITICA', 'POLITICA'),
        ('DEPORTE', 'DEPORTE'),
    )

    periodista = models.CharField(max_length=100, choices=PERIODISTA_CHOICES)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    palabra_clave = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return f'{self.periodista} - {self.categoria}'
    