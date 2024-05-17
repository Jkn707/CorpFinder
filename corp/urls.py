from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('paginaPrincipal/', views.paginaPrincipal, name='paginaPrincipal'),
    path('paginaPrincipalEmpresa/', views.paginaPrincipalEmpresa, name='paginaPrincipalEmpresa'),
    path('iniciarSesion/', views.iniciarSesion_, name='iniciarSesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('logout/', views.logout_, name='logout'),
    path('detalles/<int:id>/', views.detallesEmpresa, name='detallesEmpresa'),
    path('detalles/estadisticaEmpresa/<int:id>', views.estadisticaEmpresa, name='estadisticaEmpresa'),
    path('credenciales/', include('credenciales.urls')),
]