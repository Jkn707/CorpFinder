from django.urls import path
from . import views

urlpatterns = [
 path('credenciales/', views.credenciales, name='credenciales'),
 path('edit/', views.edit, name='edit'),
 
]