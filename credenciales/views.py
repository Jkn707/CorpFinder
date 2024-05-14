from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Credenciales

# Create your views here.

@login_required(login_url='/iniciarSesion')
def credenciales(request):
   
   crendencial = Credenciales.objects.get(usuario=request.user)
   usuario = crendencial.usuario

   return render(request,'credenciales.html',{'cred_usuario': usuario,
                                              'crendencial': crendencial})