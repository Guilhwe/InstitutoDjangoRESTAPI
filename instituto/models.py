from django.db import models
from django.core.validators import MinLengthValidator

class Estudiante(models.Model):
    nombre=models.CharField(max_length = 100)
    email =models.EmailField(blank=False, max_length=30)
    dni=models.CharField(max_length=11, unique=True)
    fecha_nacimiento=models.DateField(blank=False, null=False)
    movil=models.CharField(max_length = 9)

    def __str__(self):
        return self.nombre
class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermedio'),
        ('A','Avanzado'),
    )
    codigo=models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(3)])
    descripcion=models.CharField(max_length=100, blank=False)
    nivel=models.CharField(max_length=1,choices=NIVEL, blank=False,null=False,default='B' )
    
    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    TURNO = (
        ('M','Mañana'),
        ('T','Tarde'),
        ('N','Noche'),
    )
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso =  models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length= 1, choices= TURNO, blank =False, null=False, default='M' )