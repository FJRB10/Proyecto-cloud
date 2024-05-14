from django.contrib import admin

# Register your models here.

from .models import Projects, Usuario, Abonados, Trafico, Ingresos

admin.site.register(Projects)
admin.site.register(Usuario)
admin.site.register(Abonados)
admin.site.register(Trafico)
admin.site.register(Ingresos)