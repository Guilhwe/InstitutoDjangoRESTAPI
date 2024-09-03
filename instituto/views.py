from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudianteSerializer,EstudianteSerializerV2
from rest_framework import viewsets,generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from instituto.throttle import MatriculaAnonRateThrottle
#PARA QUE LA AUTENTIFIACION NO SEA GENERAL HAY QUE IMPORTAR EN VIEWS DESDE RESTFRAMEWORK LAS ATENTIFICACIONES Y PERMISIONES MY PONERLAS EN CADA VIEWS

class EstudianteViewSet(viewsets.ModelViewSet):
   
    queryset = Estudiante.objects.all().order_by('id')
    #serializer_class = EstudianteSerializer
    filter_backends=[DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields =['nombre',]
    search_fields = ['dni','nombre',]
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return EstudianteSerializerV2
        return EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
   
    queryset= Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    
    queryset= Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes =[UserRateThrottle, MatriculaAnonRateThrottle, ]
    http_method_names=['get', 'post',]

class ListaMatriculaEstudiante(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudiante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudianteSerializer
        
class ListaMatriculaCurso(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer