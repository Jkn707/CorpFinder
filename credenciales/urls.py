from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('credenciales/', views.credenciales, name='credenciales'),
    path('edit/', views.edit, name='edit'),
] 
