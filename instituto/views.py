from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudianteSerializer
from rest_framework import viewsets,generics

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset= Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudiante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudiante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudianteSerializer
        
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer