from django.test import TestCase
from instituto.models import Estudiante
from instituto.serializers import EstudianteSerializer

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


