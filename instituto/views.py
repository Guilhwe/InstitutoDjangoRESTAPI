from instituto.models import Estudiante,Curso,Matricula
from instituto.serializers import EstudianteSerializer,CursoSerializer,MatriculaSerializer, ListaMatriculasCursoSerializer,ListaMatriculasEstudianteSerializer,EstudianteSerializerV2
from rest_framework import viewsets,generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from instituto.throttle import MatriculaAnonRateThrottle
#PARA QUE LA AUTENTIFIACION NO SEA GENERAL HAY QUE IMPORTAR EN VIEWS DESDE RESTFRAMEWORK LAS ATENTIFICACIONES Y PERMISIONES MY PONERLAS EN CADA VIEWS

class EstudianteViewSet(viewsets.ModelViewSet):
    """
    Descripcion de la View:
   -CRUD de estudiantes
    permite filtrar por nombre los resultados

    buscar por nombre y dni
    metodo http Permitidos
    -GET POST PUT PATCH DELETE
    Clase de Serializer:
    -EstudianteSerializer: usado para la serializacion e deserializacion de datos
    -Si la version de la API fuera 'v2', usa EstudianteSerializerV2.
    """
   
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
    """
    Descripcion de la View:
    -CRUD de cursos
    metodos permitidos:
    -GET POST PUT PATCH DELETE
   
    """
   
   
    queryset= Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descripcion de la View:
   -CRUD de matriculas 
    
    -GET POST 
    Throttle classes:
    -MatriculaAnonThrottle: limite de usuarios anonimos 
    -UserRateThrottle: limite de usuarios autentificados
    
    """
   
    
    queryset= Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes =[UserRateThrottle, MatriculaAnonRateThrottle, ]
    http_method_names=['get', 'post',]

class ListaMatriculaEstudiante(generics.ListAPIView):
    """
    Descripcion de la View:
    - Lista Matriculas por id de Estudiante
    Parametros:
    - pk (int): El identificador primario del objeto. Deve ser un numero entero.
    """
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudiante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudianteSerializer
        
class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descripcion de la View:
    - Lista Matriculas por id de Curso
    Parametros:
    - pk (int): El identificador primario del objeto. Deve ser un numero entero.
    """
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer