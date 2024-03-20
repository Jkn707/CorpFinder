from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresa

# Create your views here.

def home(request):
   # return HttpResponse('<h1> Bienvenido a CorpFinder </h1>')
   # return render(request, 'home.html')
   #  return render(request, 'home.html',{'name': 'Paola Noreña'})
   searchTerm = request.GET.get('buscarEmpresa')
   if searchTerm:
      empresas = Empresa.objects.filter(nombre__icontains=searchTerm)
   else:
      empresas = Empresa.objects.all()
   return render(request,'home.html',{'searchTerm':searchTerm, 'empresas':empresas})