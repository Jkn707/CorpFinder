from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Credenciales
from django.shortcuts import get_object_or_404
from .form import MostrarTextoForm

# Create your views here.

@login_required(login_url='/iniciarSesion')
def credenciales(request):
   
   credencial = Credenciales.objects.get(usuario=request.user)
   usuario = credencial.usuario

   return render(request,'credenciales.html',{'cred_usuario': usuario,'credencial': credencial})

def cambiar_datospers(request):
   form = MostrarTextoForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():
      mostrar_input = form.cleaned_data['mostrar_input']
      texto = form.cleaned_data['texto']
      return render(request, 'credenciales.html', {'form':form,'mostrar_input':mostrar_input,'texto':texto})
   return render(request, 'credenciales.html',{'form':form})

def vista_compuesta(request):
   resultado_vista1 = cambiar_datospers(request)
   resultado_vista2 = credenciales(request)
   contenido = resultado_vista1.content + resultado_vista2.content

   return HttpResponse(contenido)