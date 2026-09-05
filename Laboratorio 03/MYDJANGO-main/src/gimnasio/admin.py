from django.contrib import admin

from .models import Asistencia, Cliente, Entrenador, Membresia, Rutina

admin.site.register([Cliente, Entrenador, Membresia, Rutina, Asistencia])
