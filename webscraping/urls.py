from django.urls import path
from . import views

urlpatterns = [
    path('scrapEmpresa/', views.ScrapEmpresa, name='scrapEmpresa'),
    path('scrapEmpresa/Resultado', views.ResultadoEmpresa, name='resultado')
]
