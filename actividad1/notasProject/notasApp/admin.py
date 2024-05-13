from django.contrib import admin
from .models import Alumno, Asignatura, Nota

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class NotaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'asignatura', 'puntaje')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Nota, NotaAdmin)