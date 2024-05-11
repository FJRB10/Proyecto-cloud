from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def paginaPrincipal(request):
    return render(request, 'html/Cod1.html')

def login(request):
    return render(request, 'html/login.html')

def perfil(request):
    return render(request, 'html/perfil.html')

def analista(request):
    return render(request, 'html/PrincipalAnalista.html')

def registro(request):
    return render(request, 'html/Registro.html')

def administrador (request):
    return render(request, 'html/Administrador.html')

def olvideContra(request):
    return render(request, 'html/OlvideContra.html')