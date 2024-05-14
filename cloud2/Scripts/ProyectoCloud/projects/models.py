import email
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length = 200)
    document = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    email = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    nombre = models.CharField(max_length = 20, null = True)
    apellido = models.CharField(max_length = 20, null = True)
    num_celular = models.CharField(max_length = 10, null = True)
    num_cedula = models.CharField(max_length = 10, null = True)
    correo = models.CharField(max_length = 30, null = True)
    contra = models.CharField(max_length = 30, null = True)
    roles = (('Usuario', 'Usuario'), ('Analista', 'Analista'), ('Administrador', 'Administrador'))
    rol = models.CharField(default = 'Usuario', choices = roles)

class Fijo_Suscriptores(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_segmento = models.IntegerField(null = True)
    segmento = models.CharField(max_length = 10, null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    id_terminal = models.IntegerField(null = True)
    terminal = models.CharField(null = True)
    id_tecnologia = models.IntegerField(null = True)
    tecnologia = models.CharField(null = True)
    cantidad_suscriptores = models.IntegerField(null = True)

class Fijo_Ingresos(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    id_segmento = models.IntegerField(null = True)
    segmento = models.CharField(max_length = 10, null = True)
    id_terminal = models.IntegerField(null = True)
    terminal = models.CharField(null = True)
    ingresos = models.IntegerField(null = True)

class Fijo_Trafico(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    trafico = models.IntegerField(null = True)

class Demanda_Ingresos(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    id_modalidad_pago = models.CharField(max_length = 3, null = True)
    modalidad_pago = models.CharField(max_length = 10, null = True)
    id_terminal = models.IntegerField(null = True)
    terminal = models.CharField(null = True)
    ingresos = models.IntegerField(null = True)

class Demanda_Abonados(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    id_modalidad_pago = models.CharField(max_length = 3, null = True)
    modalidad_pago = models.CharField(max_length = 10, null = True)
    id_terminal = models.IntegerField(null = True)
    terminal = models.CharField(null = True)
    id_tecnologia = models.IntegerField(null = True)
    tecnologia = models.CharField(null = True)
    cantidad_abonados = models.IntegerField(null = True)

class Demanda_Trafico(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    trimestre = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    id_empresa = models.IntegerField(null = True)
    empresa = models.CharField(null = True)
    id_modalidad_pago = models.CharField(max_length = 3, null = True)
    modalidad_pago = models.CharField(max_length = 10, null = True)
    trafico = models.IntegerField(null = True)