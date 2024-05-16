from django.contrib import admin
from .models import Empresa
from webscraping.models import ComentariosPropios
# Register your models here.
admin.site.register(Empresa)
admin.site.register(ComentariosPropios)
