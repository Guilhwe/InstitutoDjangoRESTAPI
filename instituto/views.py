from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer
from rest_framework import viewsets

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset= Matricula.objects.all()
    serializer_class = MatriculaSerializer