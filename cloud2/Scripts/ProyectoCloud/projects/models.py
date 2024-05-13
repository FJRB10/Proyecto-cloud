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
    roles = (('Rol', 'Usuario'), ('Rol', 'Analista'), ('Rol', 'Administrador'))
    rol = models.CharField(default = 'Usuario', choices = roles)