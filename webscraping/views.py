from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NombreEmpresa
from .computrabajo import buscarEmpresas, obtenerDatosEmpresa, obtenerComentarios
from .nlp import obtenerEmociones
from .models import Empresa, ComentariosComputrabajo

def scrapEmpresa(request):
    form = NombreEmpresa()

    if request.method == "POST":
        form = NombreEmpresa(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            opciones = buscarEmpresas(nombre)
            context = {'nombre': nombre, 'empresas_link': opciones}
            
            if opciones:
                # Almacenar los datos en la sesión para usarlos en la vista ResultadoEmpresa
                request.session['opciones'] = opciones
                request.session['nombre'] = nombre
                # Redireccionar a la página de resultados
                return redirect('resultado')
            else:
                messages.error(request, "No se encontraron empresas")

    return render(request, 'busqueda.html', {'form': form})

def resultadoEmpresa(request):
    form = NombreEmpresa()  # Instancia del formulario de búsqueda
    opciones = request.session.get('opciones')
    
    if request.method == "POST":
        # Procesar la selección de la empresa aquí
        selected_empresa = request.POST.get('selected_empresa')
        print(selected_empresa)
        if selected_empresa:
            if opciones:
                datos_empresa = obtenerDatosEmpresa(opciones[selected_empresa])
                comentarios = obtenerComentarios(opciones[selected_empresa], limite_paginas=5)
                if datos_empresa:
                    nueva_empresa = Empresa(**datos_empresa)
                    nueva_empresa.save()
                    for comentario in comentarios:
                        emocion = obtenerEmociones(comentario)
                        nuevo_comentario = ComentariosComputrabajo(fecha=comentario['fecha'], contenido=comentario['contenido'], empresa=nueva_empresa, calificacion=comentario['calificacion'], sentimiento = emocion)
                        nuevo_comentario.save()
                    messages.success(request, "Empresa guardada correctamente")
                    return redirect('scrapEmpresa')  # Redireccionar a la página ScrapEmpresa
                else:
                    messages.error(request, "No se pudieron obtener los datos de la empresa seleccionada")
            else:
                messages.error(request, "Error al obtener los datos de la empresa")
        else:
            messages.error(request, "No se seleccionó ninguna empresa")
        # Redireccionar a la página de resultados
        return redirect('resultado')

    # Obtener los datos de las empresas para mostrar en la página de resultados
    empresas = opciones if opciones else {}  # Obtén las empresas y sus enlaces
    return render(request, 'resultado.html', {'nombre': '', 'empresas_link': empresas, 'form': form})
