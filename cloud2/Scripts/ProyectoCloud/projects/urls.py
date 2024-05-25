from django.urls import path
from . import views


urlpatterns = [
    path('', views.paginaPrincipal, name = 'index'),
    path('Login', views.login, name = 'login'),
    path('login/', views.login2, name = 'login2'),
    path('Perfil', views.perfil, name = 'perfil'),
    path('PrincipalAnalista', views.PrincipalAnalista, name = 'principal_analista'),
    path('Registro', views.registro, name = 'registro'),
    path('registro/', views.usoRegistro, name = 'registro2'),
    path('Administrador', views.administrador, name = 'admin'),
    path('OlvideContra', views.olvideContra, name = 'olvideContra'),
    path('historico/', views.verHistorico, name = 'historico'),
    path('cargueArchivo/', views.cargarArchivo, name = 'cargueArchivo'),
    path('graficar/', views.graficar, name = 'graficar'),
    path('graficar2/', views.graficar2, name = 'graficar2'),
]