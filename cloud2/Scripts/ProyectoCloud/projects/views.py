from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Abonados, Trafico, Ingresos, Stenbaka_Abonados, Stenbaka_Trafico, Stenbaka_Ingresos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
import os
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from _plotly_utils import utils
import json

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
            login(user)
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
    return render(request, 'html/Perfil.html')

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
            print('Es un archivo de Excel')
        elif extension.lower() == '.csv':
            print("Es un archivo de CSV")

            csv = pd.read_csv(archivo)
            print(csv)

            if nombre_archvio == 'tabla_accesos':
                print('Es el archivo de abonados')
                long = len(csv.index)
                ultimo_registro = Abonados.objects.order_by('id').first()

                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Abonados()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Abonados()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()

            elif nombre_archvio == 'tabla_trafico':
                print('Es el archivo de trafico')
                long = len(csv.index)
                ultimo_registro = Trafico.objects.order_by('id').first()

                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Trafico()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Trafico()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()

            elif nombre_archvio == 'tabla_ingresos':
                print('Es el archivo de ingresos')
                long = len(csv.index)
                ultimo_registro = Ingresos.objects.order_by('id').first()

                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Ingresos()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Ingresos()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.colombia_telecomunicaciones = csv.iloc[i,3]
                        fila.colombia_movil = csv.iloc[i,4]
                        fila.comunicacion_celular_comcel = csv.iloc[i,5]
                        fila.empresa_de_telecomunicaciones_de_bogota = csv.iloc[i,6]
                        fila.une_epm = csv.iloc[i,7]
                        fila.avantel = csv.iloc[i,8]
                        fila.almacenes_exito = csv.iloc[i,9]
                        fila.virgin_mobile = csv.iloc[i,10]
                        fila.partners_telecom = csv.iloc[i,11]
                        fila.setroc_mobile = csv.iloc[i,12]
                        fila.uff_movil = csv.iloc[i,13]
                        fila.cellvoz_colombia = csv.iloc[i,14]
                        fila.logistica_flash = csv.iloc[i,15]
                        fila.lov_telecomunicaciones = csv.iloc[i,16]
                        fila.suma_movil = csv.iloc[i,17]
                        fila.save()

            elif nombre_archvio == 'Stenbacka_accesos':
                long = len(csv.index)
                ultimo_registro = Stenbaka_Abonados.objects.order_by('id').first()
                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Stenbaka_Abonados()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Stenbaka_Abonados()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()

            elif nombre_archvio == 'Stenbacka_trafico':
                long = len(csv.index)
                ultimo_registro = Stenbaka_Trafico.objects.order_by('id').first()
                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Stenbaka_Trafico()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Stenbaka_Trafico()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()

            elif nombre_archvio == 'Stenbacka_ingresos':
                long = len(csv.index)
                ultimo_registro = Stenbaka_Ingresos.objects.order_by('id').first()
                if ultimo_registro:
                    ultimoID = ultimo_registro.id
                    nuevoID = ultimoID + 1
                    for i in range(long):
                        fila = Stenbaka_Ingresos()
                        fila.id = nuevoID
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()
                        nuevoID += 1
                else:
                    for i in range(long):
                        fila = Stenbaka_Ingresos()
                        fila.id = i
                        fila.anio = csv.iloc[i,1]
                        fila.mes = csv.iloc[i,2]
                        fila.stenbaka = csv.iloc[i,3]
                        fila.save()

            else:
                print('No es un archivo que se deba procesar')

        else:
            return HttpResponse("<h1> Tipo de archivo no valido </h1>")
            #raise TypeError("Este tipo de archivo no es aceptado")

        #print(archivo)
        #print(type(archivo))
    return render(request, 'html/PrincipalAnalista.html')

def graficar(request):
    if request.method == 'POST':
        columna = request.POST.get('opcion')
        #print('La opción seleccionada fue: ', request.POST.get('opcion'))

        valoresAbonados = Abonados.objects.values_list(columna, flat = True)
        valoresTrafico = Trafico.objects.values_list(columna, flat = True)
        valoresIngresos = Ingresos.objects.values_list(columna, flat = True)

        anios = Abonados.objects.values_list('anio', flat = True)
        meses = Abonados.objects.values_list('mes', flat = True)

        fechas = []

        for i in range(len(anios)):
            fechas.append(str(anios[i]) + "-" + str(meses[i]) + "-01")

        #print(fechas)

        fig = go.Figure()
        fig2 = go.Figure()
        fig3 = go.Figure()

        fig.add_trace(go.Scatter(x = fechas, y = list(valoresAbonados), mode = 'lines+markers', name = 'Valores'))
        fig2.add_trace(go.Scatter(x = fechas, y = list(valoresTrafico), mode = 'lines+markers', name = 'Valores'))
        fig3.add_trace(go.Scatter(x = fechas, y = list(valoresIngresos), mode = 'lines+markers', name = 'Valores'))

        fig.update_layout(title = f'Grafica de abonados de {columna}', xaxis_title = 'Meses', yaxis_title = 'Abonados')
        fig2.update_layout(title = f'Grafica de trafico de {columna}', xaxis_title = 'Meses', yaxis_title = 'Trafico')
        fig3.update_layout(title = f'Grafica de ingresos de {columna}', xaxis_title = 'Meses', yaxis_title = 'Ingresos')

        graph1_html = fig.to_html(full_html = False, default_height=600, default_width=1750)
        graph2_html = fig2.to_html(full_html = False, default_height=600, default_width=1750)
        graph3_html = fig3.to_html(full_html = False, default_height=600, default_width=1750)

        return render(request, 'html/PrincipalAnalista.html', {'grafica1': graph1_html, 'grafica2': graph2_html, 'grafica3': graph3_html})
        #return HttpResponse('El view funciona')
    else:
        print('El view no sirve')
        return HttpResponse('El view no funciona')

def graficar2(request):
    if request.method == 'POST':
        print("Si se enviaron los datos")
        valoresStenbackAbonados = Stenbaka_Abonados.objects.values_list('stenbaka', flat = True)
        valoresStenbackTrafico = Stenbaka_Trafico.objects.values_list('stenbaka', flat = True)
        valoresStenbackIngresos = Stenbaka_Ingresos.objects.values_list('stenbaka', flat = True)

        anios = Stenbaka_Abonados.objects.values_list('anio', flat = True)
        meses = Stenbaka_Abonados.objects.values_list('mes', flat = True)

        fechas = []

        for i in range(len(anios)):
            fechas.append(str(anios[i]) + "-" + str(meses[i]) + "-01")

        fig1 = go.Figure()
        fig2 = go.Figure()
        fig3 = go.Figure()

        fig1.add_trace(go.Scatter(x = fechas, y = list(valoresStenbackAbonados), mode = 'lines+markers', name = 'Valores'))
        fig2.add_trace(go.Scatter(x = fechas, y = list(valoresStenbackTrafico), mode = 'lines+markers', name = 'Valores'))
        fig3.add_trace(go.Scatter(x = fechas, y = list(valoresStenbackIngresos), mode = 'lines+markers', name = 'Valores'))

        fig1.update_layout(title = f'Grafica de Stenbacka de abonados', xaxis_title = 'Meses', yaxis_title = 'Stenbacka de Abonados')
        fig2.update_layout(title = f'Grafica Stenbacka de trafico', xaxis_title = 'Meses', yaxis_title = 'Stenbacka de Trafico')
        fig3.update_layout(title = f'Grafica Stenbacka de ingresos', xaxis_title = 'Meses', yaxis_title = 'Stenbacka de Ingresos')

        graph1_1_html = fig1.to_html(full_html = False, default_height=600, default_width=1750)
        graph2_2_html = fig2.to_html(full_html = False, default_height=600, default_width=1750)
        graph3_3_html = fig3.to_html(full_html = False, default_height=600, default_width=1750)

        return render(request, 'html/PrincipalAnalista.html', {
            'grafica1_1': graph1_1_html, 
            'grafica2_2': graph2_2_html, 
            'grafica3_3': graph3_3_html,
        })
    else:
        return HttpResponse('El view no funciona')