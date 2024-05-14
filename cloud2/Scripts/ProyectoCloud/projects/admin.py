from django.contrib import admin

# Register your models here.

from .models import Projects, Usuario, Fijo_Suscriptores

admin.site.register(Projects)
admin.site.register(Usuario)
admin.site.register(Fijo_Suscriptores)