from django.db import models
from datetime import datetime

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=200, null=True)
    logo_empresa = models.URLField(blank=True, null=True)
    banner_empresa = models.URLField(blank=True, null=True)

    subtitle = models.CharField(max_length=255, blank=True, null=True)
    subtitle_content = models.TextField(blank=True, null=True)
    subtitle2 = models.CharField(max_length=255, blank=True, null=True)
    subtitle2_content = models.TextField(blank=True, null=True)

    # Estadísticas
    seguidores = models.IntegerField(default=0, null=True)
    extraido_de = models.CharField(max_length=255, blank=True, null=True)
    Fecha_extraccion = models.DateField(default=datetime.now().date().isoformat(), null=True)

    # Ofertas de trabajo
    numero_ofertas = models.IntegerField(default=0, null=True)

    # Evaluaciones
    numero_evaluaciones = models.IntegerField(default=0, null=True)

    # Salarios
    numero_salarios = models.IntegerField(default=0, null=True)

    # Entrevistas
    numero_entrevistas = models.IntegerField(default=0, null=True)

    # Beneficios
    numero_beneficios = models.IntegerField(default=0, null=True)

    # Multimedia
    numero_fotos = models.IntegerField(default=0, null=True)

    # Valoración
    calificacion_empresa = models.FloatField(default=0.0, null=True)

    def __str__(self):
        return self.nombre_empresa