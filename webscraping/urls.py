from django.urls import path
from . import views

urlpatterns = [
    path('scrapEmpresa/', views.scrapEmpresa, name='scrapEmpresa'),
    path('scrapEmpresa/Resultado', views.resultadoEmpresa, name='resultado')
]
