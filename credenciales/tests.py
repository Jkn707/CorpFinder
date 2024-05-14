from django.test import TestCase

# Create your tests here.

from models import Credenciales

def mostrar_credenciales():
    # Obtener el único objeto Credenciales
    credenciales = Credenciales.objects.first()  # Suponiendo que solo haya un objeto Credenciales en la base de datos

    # Verificar si se encontró un objeto Credenciales
    if credenciales:
        # Imprimir todos los atributos del objeto Credenciales en la consola
        print("Usuario:", credenciales.usuario)
        print("Imagen:", credenciales.imagen.url)
        print("Redes:", credenciales.redes)
        print("Empresas favoritas:")
        for empresa in credenciales.empresas_favoritas.all():
            print("- Nombre:", empresa.nombre)
            print("  Descripción:", empresa.descripcion)
            # Agrega más atributos según sea necesario
        print("Archivo PDF:", credenciales.archivo_pdf.url if credenciales.archivo_pdf else "N/A")
        # Agrega más atributos según sea necesario
    else:
        # Manejar el caso en que no se encuentre ningún objeto Credenciales
        print("No se encontró ningún objeto Credenciales en la base de datos.")

# Llamar a la función para mostrar los atributos de Credenciales
mostrar_credenciales()

