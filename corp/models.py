from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1),MaxValueValidator(999_999_999)], unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=50, default='N/A')
    ubicacion = models.CharField(max_length=100, default = 'N/A')
    salario = models.CharField(max_length = 10, default = '0')
    nivel_marca_empleadora = models.CharField(max_length = 50, default = 'Marca empleadora estandar')
    calificacion = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    imagen = models.ImageField(upload_to='corp/images/', default='corp/images/default.png')
    redes = models.TextField(default = 'N/A')