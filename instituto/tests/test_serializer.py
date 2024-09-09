from django.test import TestCase
from instituto.models import Estudiante, Curso, Matricula
from instituto.serializers import EstudianteSerializer, CursoSerializer,MatriculaSerializer


class SerializerEstudianteTestCase(TestCase):
    def setUp(self):
        self.estudiante = Estudiante(
            nombre ='Test de Modelo',
            email= 'testdemodelo@gmail.com',
            dni='1234567891p',
            fecha_nacimiento ='2023-02-02',
            movil='123456789',
        )
        self.serializer_estudiante = EstudianteSerializer(instance=self.estudiante)
    
    def test_verifica_campos_serializados_de_estudiante(self):
        '''Test que verifica los campos que estan siendo serializados de estudiante'''
        datos = self.serializer_estudiante.data
        self.assertEqual(set(datos.keys()),set(['id','nombre', 'email', 'dni', 'fecha_nacimiento', 'movil',]))

    def test_verifica_contenido_de_los_campos_serializados_de_estudiante(self):
        '''Test que verifica los contenidos de los campos que estan siendo serializados de estudiante'''
        datos = self.serializer_estudiante.data
        self.assertEqual(datos['nombre'],self.estudiante.nombre)
        self.assertEqual(datos['email'],self.estudiante.email)
        self.assertEqual(datos['dni'],self.estudiante.dni)
        self.assertEqual(datos['fecha_nacimiento'],self.estudiante.fecha_nacimiento)
        self.assertEqual(datos['movil'],self.estudiante.movil)


class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo = 'CTM',
            descripcion = 'Curso Test Modelo',
            nivel = 'B',
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        """Teste que verifica los campos que estan siendo serializados de curso"""
        datos = self.serializer_curso.data
        self.assertEqual(set(datos.keys()),set(['id','codigo','descripcion','nivel']))  
    
    def test_verifica_contenido_de_los_campos_serializados_de_estudiante(self):
        """Test que verifica el contenido de los campos que estan siendo serializados de estudiante"""
        datos = self.serializer_curso.data
        self.assertEqual(datos['codigo'],self.curso.codigo)
        self.assertEqual(datos['descripcion'],self.curso.descripcion)
        self.assertEqual(datos['nivel'],self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudiante_matricula = Estudiante.objects.create(
            nombre = 'Test Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            dni='345567123h',
            fecha_nacimiento='2003-02-02',
            movil='655367267'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descripcion='Curso Test Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudiante=self.estudiante_matricula,
            curso=self.curso_matricula,
            turno='M'
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
    def test_verifica_campos_serializados_de_matricula(self):
        """Test que verifica los campos que estan siendo serializados de matricula"""
        datos = self.serializer_matricula.data
        self.assertEqual(set(datos.keys()),set(['id','estudiante','curso','turno']))  
    
    def test_verifica_contenido_de_los_campos_serializados_de_estudante(self):
        """Test que verifica el contenido de los campos que estan siendo serializados de estudiante"""
        datos = self.serializer_matricula.data
        self.assertEqual(datos['estudiante'],self.matricula.estudiante.id)
        self.assertEqual(datos['curso'],self.matricula.curso.id)
        self.assertEqual(datos['turno'],self.matricula.turno)
