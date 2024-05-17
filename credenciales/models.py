from django.db import models
from django.contrib.auth.models import User
from webscraping.models import Empresa
from django.db.models.signals import post_save
# Create your models here.

class Credenciales(models.Model):
    #relaciono Uno a Uno Users con credenciales
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='credenciales', default=None)
    #campo de imagen
    imagen = models.ImageField(upload_to='credenciales/images/', default='credenciales/images/image_5.png',blank=True)
    #campo de redes sociales
    redes = models.TextField(default = 'N/A')  
    #hoja de vida
    CV = models.FileField(null=True, blank=True)
    #sección de empresas favoritas
    empresas_favoritas = models.ManyToManyField(Empresa, blank=True)
    
#Esta función crea automáticamente un objeto de Credenciales asociado cuando se crea un nuevo usuario.
def crear_credencial_usuario(sender, instance, created, **kwargs):

    if created:
         Credenciales.objects.create(usuario=instance)

#Esta función guarda automáticamente el perfil de usuario después de que se guarda el objeto User.
def guardar_credencial_usuario(sender, instance, **kwargs): 
    instance.credenciales.save()

# Estas 2 líneas de código conectan las funciones a las señales post_save para el modelo User.
# Cuando se crea o actualiza un objeto User, estas funciones se ejecutan automáticamente.

post_save.connect(crear_credencial_usuario, sender=User)
post_save.connect(guardar_credencial_usuario, sender=User)


