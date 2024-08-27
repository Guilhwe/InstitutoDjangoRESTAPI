from django.db import models

class Estudiante(models.Model):
    nombre=models.CharField(max_lenght = 50)
    email =models.EmailField(blank=False, max_length=30)
    dni=models.CharField(max_length=11)
    fecha_nacimiento=models.DateField
    movil=models.CharField(max_lenght = 9)

    def __str__(self):
        return self.nombre
class Curso(models.Model)
