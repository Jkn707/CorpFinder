from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('credenciales/', views.credenciales, name='credenciales'),
    path('edit/', views.edit, name='edit'),
    path('agregar_empresa_fav/<int:id>/', views.agregar_empresa_fav, name='agregar_empresa_fav'),
    path('quitar_empresa_fav/<int:id>/', views.quitar_empresa_fav, name='quitar_empresa_fav') 
] 
