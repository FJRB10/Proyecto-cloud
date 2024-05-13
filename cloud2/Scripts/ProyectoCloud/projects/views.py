from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.models import User

# Create your views here.

def paginaPrincipal(request):
    return render(request, 'html/Cod1.html')

def login(request):
    return render(request, 'html/login.html')

def perfil(request):
    return render(request, 'html/perfil.html')

def PrincipalAnalista(request):
    return render(request, 'html/PrincipalAnalista.html')

def registro(request):
    return render(request, 'html/Registro.html')

def usoRegistro(request):
    print(request.POST)
    print('Nombre:', request.POST['Nombre'])
    print('Apellido:', request.POST['Apellido'])
    print('Número de celular:', request.POST['NumeroCel'])
    print('Número de cedula:', request.POST['NumeroCedu'])
    print('Correo:', request.POST['Email'])
    print('Contraseña:', request.POST['Contraseña'])

    if User.objects.filter(username = request.POST['Email']).exists():
        return HttpResponse("<h1>ERROR</h1>"
                            "<h1>Usuario ya existe</h1>")
    if Usuario.objects.filter(num_celular = request.POST['NumeroCel']).exists():
        return HttpResponse("<h1>ERROR</h1>"
                            "<h1>Número de celular ya existe</h1>")
    if Usuario.objects.filter(num_cedula = request.POST['NumeroCedu']).exists():
        return HttpResponse("<h1>ERROR</h1>"
                            "<h1>Cedula ya existe</h1>")

    user1 = User()
    user1.is_superuser = False
    user1.username = request.POST['Email']
    user1.first_name = request.POST['Nombre']
    user1.last_name = request.POST['Apellido']
    user1.email = request.POST['Email']
    user1.is_staff = False
    user1.is_active = True
    user1.set_password(request.POST['Contraseña'])
    user1.save()

    user2 = Usuario()
    user2.usuario_id = user1.id
    user2.nombre = request.POST['Nombre']
    user2.apellido = request.POST['Apellido']
    user2.num_celular = request.POST['NumeroCel']
    user2.num_cedula = request.POST['NumeroCedu']
    user2.correo = request.POST['Email']
    user2.contra = request.POST['Contraseña']
    user2.rol = 'Analista'
    user2.save()

    return redirect('/Registro.html')

def administrador (request):
    return render(request, 'html/Administrador.html')

def olvideContra(request):
    return render(request, 'html/OlvideContra.html')