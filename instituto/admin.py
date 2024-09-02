from django.contrib import admin
from instituto.models import Estudiante,Curso,Matricula

class Estudiantes(admin.ModelAdmin):
    list_display = ('id','nombre', 'email','dni','fecha_nacimiento','movil')
    list_display_links=('id','nombre',)
    list_per_page =20
    search_fields=('nombre',)
    ordering =('nombre',)

admin.site.register(Estudiante, Estudiantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo','descripcion')
    list_display_links=('id','codigo',)
    search_fields=('codigo',)

admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id','estudiante','curso','turno')
    list_display_links=('id',)

admin.site.register(Matricula,Matriculas)