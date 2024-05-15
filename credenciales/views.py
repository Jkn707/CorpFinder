from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Credenciales
from django.shortcuts import get_object_or_404
from .form import UserForm, CredencialForm

# Create your views here.

@login_required(login_url='/iniciarSesion')
def credenciales(request):
   
   credencial = Credenciales.objects.get(usuario=request.user)
   usuario = credencial.usuario

   return render(request,'credenciales.html',{'cred_usuario': usuario,'credencial': credencial})

def edit(request):
    user_form = UserForm(instance=request.user)
    credencial = Credenciales.objects.get(usuario=request.user)
    credencial_form = CredencialForm(instance=credencial)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        credencial_form = CredencialForm(request.POST, instance=request.user.credencial)
        if user_form.is_valid() and credencial_form.is_valid():
            user_form.save()
            credencial_form.save()
            return redirect('credenciales')  # Redirige a la página de perfil después de guardar los cambios

    return render(request, 'edit.html', {'user_form': user_form, 'credencial_form': credencial_form})
