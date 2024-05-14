from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse,HttpRequest
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Empresa

User = get_user_model()

# Create your views here.

@login_required(login_url='/iniciarSesion')
def paginaPrincipal(request):
   # return HttpResponse('<h1> Bienvenido a CorpFinder </h1>')
   # return render(request, 'home.html')
   #  return render(request, 'home.html',{'name': 'Paola Noreña'})
   searchTerm = request.GET.get('buscarEmpresa')
   if searchTerm:
      empresas = Empresa.objects.filter(nombre__icontains=searchTerm)
   else:
      empresas = Empresa.objects.all()
   return render(request,'paginaPrincipal.html',{'searchTerm':searchTerm, 'empresas':empresas})


@login_required(login_url='/iniciarSesion')
def paginaPrincipalEmpresa(request):
   # return HttpResponse('<h1> Bienvenido a CorpFinder </h1>')
   # return render(request, 'home.html')
   #  return render(request, 'home.html',{'name': 'Paola Noreña'})
   searchTerm = request.GET.get('buscarEmpresa')
   if searchTerm:
      empresas = Empresa.objects.filter(nombre__icontains=searchTerm)
   else:
      empresas = Empresa.objects.all()
   return render(request,'paginaPrincipalEmpresa.html',{'searchTerm':searchTerm, 'empresas':empresas})


def home(request):
   return render(request,'home.html')


def iniciarSesion_(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                opcion =form.cleaned_data.get('Tipo')
                if opcion == 'Empresa':
                    return redirect("/paginaPrincipalEmpresa")
                elif opcion == 'Persona':
                    return redirect("/paginaPrincipal")

    context = {'loginform':form}    
    return render(request,'iniciarSesion.html', context=context)

def registrarse(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/iniciarSesion")
        
    context = {'registerform' : form}

    return render(request,'registrarse.html', context=context)


def logout_(request):
    logout(request)
    return redirect("/")

