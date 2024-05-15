from django.urls import path
from . import views

urlpatterns = [
 path('credenciales/', views.vista_compuesta, name='credenciales'),
 
]