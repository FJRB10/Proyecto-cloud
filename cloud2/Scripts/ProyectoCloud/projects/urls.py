from django.urls import path
from . import views


urlpatterns = [
    path('Cod1.html', views.paginaPrincipal, name = 'projects'),
    path('Login.html', views.login, name = 'project'),
    path('Perfil.html', views.perfil, name = 'project'),
    path('PrincipalAnalista.html', views.PrincipalAnalista, name = 'project'),
    path('Registro.html', views.registro, name = 'project'),
    path('registro/', views.usoRegistro),
    path('Administrador.html', views.administrador, name = 'project'),
    path('OlvideContra.html', views.olvideContra, name = 'project'),
]