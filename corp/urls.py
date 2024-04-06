from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('paginaPrincipal/', views.paginaPrincipal, name='paginaPrincipal'),
    path('iniciarSesion/', views.iniciarSesion_, name='iniciarSesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('logout/', views.logout_, name='logout')
]