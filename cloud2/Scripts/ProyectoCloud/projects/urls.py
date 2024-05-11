from django.urls import path
from . import views


urlpatterns = [
    path('', views.paginaPrincipal, name = 'projects'),
    path('Login.html', views.login, name = 'project'),
    path('Perfil.html', views.perfil, name = 'project'),
    path('analista', views.analista, name = 'project'),
    path('Registro.html', views.registro, name = 'project'),
    path('Administrador.html', views.administrador, name = 'project'),
    path('OlvideContra.html', views.olvideContra, name = 'project'),
]