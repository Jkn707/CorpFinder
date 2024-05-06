# En el archivo webscraping/management/commands/borrar.py
# Para borrar todo lo de una tabla

from django.core.management.base import BaseCommand
from webscraping.models import Empresa

class Command(BaseCommand):
    help = 'Borra todos los datos de la tabla MiModelo'

    def handle(self, *args, **kwargs):
        # Borrar todos los datos de la tabla MiModelo
        Empresa.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Datos de la tabla Empresa borrados exitosamente'))
