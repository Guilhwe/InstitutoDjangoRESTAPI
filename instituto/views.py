from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudianteSerializer
from rest_framework import viewsets,generics, filters
from django_filters.rest_framework import DjangoFilterBackend
#PARA QUE LA AUTENTIFIACION NO SEA GENERAL HAY QUE IMPORTAR EN VIEWS DESDE RESTFRAMEWORK LAS ATENTIFICACIONES Y PERMISIONES MY PONERLAS EN CADA VIEWS

class EstudianteViewSet(viewsets.ModelViewSet):
   
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends=[DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields =['nombre',]
    search_fields = ['dni',]

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