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

class Abonados(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    colombia_telecomunicaciones = models.BigIntegerField(null = True)
    colombia_movil = models.BigIntegerField(null = True)
    comunicacion_celular_comcel = models.BigIntegerField(null = True)
    empresa_de_telecomunicaciones_de_bogota = models.BigIntegerField(null = True)
    une_epm = models.BigIntegerField(null = True)
    avantel = models.BigIntegerField(null = True)
    almacenes_exito = models.BigIntegerField(null = True)
    virgin_mobile = models.BigIntegerField(null = True)
    partners_telecom = models.BigIntegerField(null = True)
    setroc_mobile = models.BigIntegerField(null = True)
    uff_movil = models.BigIntegerField(null = True)
    cellvoz_colombia = models.BigIntegerField(null = True)
    logistica_flash = models.BigIntegerField(null = True)
    lov_telecomunicaciones = models.BigIntegerField(null = True)
    suma_movil = models.BigIntegerField(null = True)

class Trafico(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    colombia_telecomunicaciones = models.BigIntegerField(null = True)
    colombia_movil = models.BigIntegerField(null = True)
    comunicacion_celular_comcel = models.BigIntegerField(null = True)
    empresa_de_telecomunicaciones_de_bogota = models.BigIntegerField(null = True)
    une_epm = models.BigIntegerField(null = True)
    avantel = models.BigIntegerField(null = True)
    almacenes_exito = models.BigIntegerField(null = True)
    virgin_mobile = models.BigIntegerField(null = True)
    partners_telecom = models.BigIntegerField(null = True)
    setroc_mobile = models.BigIntegerField(null = True)
    uff_movil = models.BigIntegerField(null = True)
    cellvoz_colombia = models.BigIntegerField(null = True)
    logistica_flash = models.BigIntegerField(null = True)
    lov_telecomunicaciones = models.BigIntegerField(null = True)
    suma_movil = models.BigIntegerField(null = True)

class Ingresos(models.Model):
    id = models.IntegerField(primary_key = True)
    anio = models.IntegerField(null = True)
    mes = models.IntegerField(null = True)
    colombia_telecomunicaciones = models.BigIntegerField(null = True)
    colombia_movil = models.BigIntegerField(null = True)
    comunicacion_celular_comcel = models.BigIntegerField(null = True)
    empresa_de_telecomunicaciones_de_bogota = models.BigIntegerField(null = True)
    une_epm = models.BigIntegerField(null = True)
    avantel = models.BigIntegerField(null = True)
    almacenes_exito = models.BigIntegerField(null = True)
    virgin_mobile = models.BigIntegerField(null = True)
    partners_telecom = models.BigIntegerField(null = True)
    setroc_mobile = models.BigIntegerField(null = True)
    uff_movil = models.BigIntegerField(null = True)
    cellvoz_colombia = models.BigIntegerField(null = True)
    logistica_flash = models.BigIntegerField(null = True)
    lov_telecomunicaciones = models.BigIntegerField(null = True)
    suma_movil = models.BigIntegerField(null = True)