from django.contrib import admin

# Register your models here.

from .models import Projects, Usuario

admin.site.register(Projects)
admin.site.register(Usuario)