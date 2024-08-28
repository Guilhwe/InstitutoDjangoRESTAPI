from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudianteSerializer
from rest_framework import viewsets,generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudianteViewSet(viewsets.ModelViewSet):
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset= Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudiante(generics.ListAPIView):
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudiante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudianteSerializer
        
class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer