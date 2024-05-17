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
    path('detallesEmpresas/<int:id>/', views.detallesEmpresaEmpresa, name='detallesEmpresaEmpresa'),
    path('detalles/estadisticaEmpresa/<int:id>', views.estadisticaEmpresa, name='estadisticaEmpresa'),
    path('borrar_comentario/<int:id>/', views.borrar_comentario, name='borrar_comentario'),
    path('borrar_comentario_p/<int:id>/', views.borrar_comentario_p, name='borrar_comentario_p'),
    path('credenciales/', include('credenciales.urls')),
    path('reportCT/<int:id>/', views.reportarComentarioCT, name='reportarComentarioCT'),
    path('reportCP/<int:id>/', views.reportarComentarioPropio, name='reportarComentarioPropio'),
]