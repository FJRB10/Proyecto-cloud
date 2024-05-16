from django.urls import path
from . import views


urlpatterns = [
    path('Cod1.html', views.paginaPrincipal, name = 'projects'),
    path('Login.html', views.login, name = 'project'),
    path('login/', views.login2),
    path('Perfil.html', views.perfil, name = 'project'),
    path('PrincipalAnalista.html', views.PrincipalAnalista, name = 'project'),
    path('Registro.html', views.registro, name = 'project'),
    path('registro/', views.usoRegistro),
    path('Administrador.html', views.administrador, name = 'project'),
    path('OlvideContra.html', views.olvideContra, name = 'project'),
    path('historico/', views.verHistorico),
    path('cargueArchivo/', views.cargarArchivo),
    path('graficar/', views.graficar),
]