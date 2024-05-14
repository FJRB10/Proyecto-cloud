from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Fijo_Suscriptores, Fijo_Ingresos, Fijo_Trafico, Demanda_Ingresos, Demanda_Abonados, Demanda_Trafico
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
import os
import pandas as pd

# Create your views here.

def paginaPrincipal(request):
    #if request.user.is_anonymous:
        #return redirect('/Login.html')
    #else:
        return render(request, 'html/Cod1.html')

def login(request):
    #print(request.user)
    return render(request, 'html/login.html')

def login2(request):
    if request.method == 'POST':
        username = request.POST['correo']
        password = request.POST['contraseña']

        print(request.POST)

        user = authenticate(request, username = username, password = password)

        print('Usuario:', user)
        print('Esta activo?', user.is_active)
        print('Es anonimo?', user.is_anonymous)

        if user is not None:
            print('Se dirige hacer el login')
            login(request, user)
            user2 = Usuario.objects.get(correo = user).rol
            print(user2)
            

            if user2 == 'Usuario':
                return redirect('/Cod1.html')
            elif user2 == 'Analista':
                return redirect('/PrincipalAnalista.html')
            else:
                return redirect('/Administrador.html')
        else:
            print('No realiza el login')
            return redirect('/Login.html')

def perfil(request):
    return render(request, 'html/perfil.html')

def PrincipalAnalista(request):
    #print(request.user)
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
    user1.is_staff = True
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
    user2.rol = 'Usuario'
    user2.save()

    return redirect('/Registro.html')

def administrador (request):
    return render(request, 'html/Administrador.html')

def olvideContra(request):
    return render(request, 'html/OlvideContra.html')

#@login_required
def verHistorico(request):
    print(request.user.is_authenticated)
    print(request.user)
    print(request.user.username)
    return HttpResponse("El boton esta funcionando")

def cargarArchivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']

        nombre_archvio, extension = os.path.splitext(archivo.name)

        if extension.lower() == '.xlsx':
            excel = pd.read_excel(archivo, sheet_name = None)
            pag1 = 'INTERNET_MOVIL_CARGO_FIJO_SUSCR'
            pag2 = 'INTERNET_MOVIL_CARGO_FIJO_INGRE'
            pag3 = 'INTERNET_MOVIL_CARGO_FIJO_TRAFI'
            pag4 = 'INTERNET_MOVIL_DEMANDA_INGRESOS'
            pag5 = 'INTERNET_MOVIL_DEMANDA_ABONADOS'
            pag6 = 'INTERNET_MOVIL_DEMANDA_TRAFICO_'

            lista = [pag1, pag2, pag3, pag4, pag5, pag6]
            
            for i in lista:
                try:
                    excel[i]
                    
                    if i == pag1:
                        print(excel[i].iloc[0])
                        long = len(excel[i].index)

                        ultimo_registro = Fijo_Suscriptores.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Fijo_Suscriptores()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idSegmento = excel[i].iloc[j,3]
                                fila.segmento = excel[i].iloc[j,4]
                                fila.idEmpresa = excel[i].iloc[j,5]
                                fila.empresa = excel[i].iloc[j,6]
                                fila.idterminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.idtecnologia = excel[i].iloc[j,9]
                                fila.tecnologia = excel[i].iloc[j,10]
                                fila.cantidadSus = excel[i].iloc[j,11]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Fijo_Suscriptores()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idSegmento = excel[i].iloc[j,3]
                                fila.segmento = excel[i].iloc[j,4]
                                fila.idEmpresa = excel[i].iloc[j,5]
                                fila.empresa = excel[i].iloc[j,6]
                                fila.idterminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.idtecnologia = excel[i].iloc[j,9]
                                fila.tecnologia = excel[i].iloc[j,10]
                                fila.cantidadSus = excel[i].iloc[j,11]
                                fila.save()

                    elif i == pag2:
                        long = len(excel[i].index)

                        ultimo_registro = Fijo_Ingresos.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Fijo_Ingresos()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.idSegmento = excel[i].iloc[j,5]
                                fila.segmento = excel[i].iloc[j,6]
                                fila.idterminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.ingresos = excel[i].iloc[j,9]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Fijo_Ingresos()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.idSegmento = excel[i].iloc[j,5]
                                fila.segmento = excel[i].iloc[j,6]
                                fila.idterminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.ingresos = excel[i].iloc[j,9]
                                fila.save()

                    elif i == pag3:
                        long = len(excel[i].index)

                        ultimo_registro = Fijo_Trafico.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Fijo_Trafico()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.trafico = excel[i].iloc[j,5]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Fijo_Trafico()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.trafico = excel[i].iloc[j,5]
                                fila.save()

                    elif i == pag4:
                        long = len(excel[i].index)

                        ultimo_registro = Demanda_Ingresos.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Demanda_Ingresos()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,5]
                                fila.modalidad_pago = excel[i].iloc[j,6]
                                fila.id_terminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.ingresos = excel[i].iloc[j,9]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Demanda_Ingresos()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,5]
                                fila.modalidad_pago = excel[i].iloc[j,6]
                                fila.id_terminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.ingresos = excel[i].iloc[j,9]
                                fila.save()

                    elif i == pag5:
                        long = len(excel[i].index)

                        ultimo_registro = Demanda_Abonados.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Demanda_Abonados()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,5]
                                fila.modalidad_pago = excel[i].iloc[j,6]
                                fila.id_terminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.id_tecnologia = excel[i].iloc[j,9]
                                fila.tecnologia = excel[i].iloc[j,10]
                                fila.cantidad_abonados = excel[i].iloc[j,11]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Demanda_Abonados()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,5]
                                fila.modalidad_pago = excel[i].iloc[j,6]
                                fila.id_terminal = excel[i].iloc[j,7]
                                fila.terminal = excel[i].iloc[j,8]
                                fila.id_tecnologia = excel[i].iloc[j,9]
                                fila.tecnologia = excel[i].iloc[j,10]
                                fila.cantidad_abonados = excel[i].iloc[j,11]
                                fila.save()
                    
                    elif i == pag6:
                        long = len(excel[i].index)

                        ultimo_registro = Demanda_Trafico.objects.order_by('id').first()

                        if ultimo_registro:
                            print(f'La tabla {i} tiene elementos\n')
                            ultimoID = ultimo_registro.id
                            nuevoID = ultimoID + 1
                            for j in range(long):
                                fila = Demanda_Trafico()
                                fila.id = nuevoID
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,7]
                                fila.modalidad_pago = excel[i].iloc[j,5]
                                fila.trafico = excel[i].iloc[j,6]
                                fila.save()
                                nuevoID += 1
                        else:
                            print(f'la tabla {i} esta vacia')
                            for j in range(long):
                                fila = Demanda_Trafico()
                                fila.id = j
                                fila.anio = excel[i].iloc[j,0]
                                fila.trimestre = excel[i].iloc[j,1]
                                fila.mes = excel[i].iloc[j,2]
                                fila.idEmpresa = excel[i].iloc[j,3]
                                fila.empresa = excel[i].iloc[j,4]
                                fila.id_modalidad_pago = excel[i].iloc[j,7]
                                fila.modalidad_pago = excel[i].iloc[j,5]
                                fila.trafico = excel[i].iloc[j,6]
                                fila.save()

                except KeyError:
                    print("ERROR")
            
            print('Es un archivo de Excel')
        elif extension.lower() == '.csv':
            print("Es un archivo de CSV")
        else:
            return HttpResponse("<h1> Tipo de archivo no valido </h1>")
            #raise TypeError("Este tipo de archivo no es aceptado")

        #print(archivo)
        #print(type(archivo))
    return HttpResponse("El boton esta funcionando")