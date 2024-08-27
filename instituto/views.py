from instituto.models import Estudiante,Curso
from instituto.serializers import EstudianteSerializer,CursoSerializer
from rest_framework import viewsets

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer