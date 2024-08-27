from django.db import models

class Estudiante(models.Model):
    nombre=models.CharField(max_length = 100)
    email =models.EmailField(blank=False, max_length=30)
    dni=models.CharField(max_length=11)
    fecha_nacimiento=models.DateField
    movil=models.CharField(max_length = 9)

    def __str__(self):
        return self.nombre
class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermedio'),
        ('A','Avanzado'),
    )
    codigo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100, blank=False)
    nivel=models.CharField(max_length=1,choices=NIVEL, blank=False,null=False,default='B' )
    
    def __str__(self):
        return self.codigo