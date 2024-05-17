from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Credenciales
from django.shortcuts import get_object_or_404
from .form import UserForm, CredencialForm
from webscraping.models import Empresa
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@login_required(login_url='/iniciarSesion')
def credenciales(request):
   usuario_actual = Credenciales.objects.get(usuario_id=request.user.id)
   credencial = Credenciales.objects.get(usuario=request.user)
   usuario = credencial.usuario

   return render(request,'credenciales.html',{'cred_usuario': usuario,'credencial': credencial, 'usuario_actual': usuario_actual})

def edit(request):
    usuario_actual = Credenciales.objects.get(usuario_id=request.user.id)
    user_form = UserForm(instance=request.user)
    credencial = Credenciales.objects.get(usuario=request.user)
    credencial_form = CredencialForm(instance=credencial)
    print('editar')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        credencial_form = CredencialForm(request.POST, request.FILES, instance=credencial)

        if user_form.is_valid() and credencial_form.is_valid():
            user_form.save()
            credencial_form.save()

            # Actualizar la sesión del usuario si la contraseña ha cambiado
            if user_form.cleaned_data.get("new_password"):
                update_session_auth_hash(request, request.user)

            # Verificar si se ha subido una nueva imagen
            if 'imagen' in request.FILES:
                credencial.imagen = request.FILES['imagen']
                credencial.save()

            # Verificar si se ha subido un nuevo CV
            if 'CV' in request.FILES:
                credencial.CV = request.FILES['CV']
                credencial.save()

            return redirect('credenciales')  # Redirige a la página de perfil después de guardar los cambios

    return render(request, 'edit.html', {
        'user_form': user_form,
        'credencial_form': credencial_form,
        'usuario_actual': usuario_actual,
    })

def agregar_empresa_fav(request,id): 
    if request.method == 'POST':
            empresa = get_object_or_404(Empresa, id=id)        
            credencial = Credenciales.objects.get(usuario=request.user)  # Obtén las credenciales del usuario actual
            credencial.empresas_favoritas.add(empresa)  # Agrega la empresa a las empresas favoritas del usuario
            credencial.save()
            return redirect('paginaPrincipal') 
    return redirect('paginaPrincipal') 

def quitar_empresa_fav(request,id):
    if request.method == 'POST':
            empresa = get_object_or_404(Empresa, id=id)        
            credencial = Credenciales.objects.get(usuario=request.user)  # Obtén las credenciales del usuario actual
            credencial.empresas_favoritas.remove(empresa)  # Quita la empresa a las empresas favoritas del usuario
            credencial.save()
            return redirect('paginaPrincipal') 
    return redirect('paginaPrincipal') 