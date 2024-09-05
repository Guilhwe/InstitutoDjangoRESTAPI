from django.test import TestCase
from instituto.models import Estudiante

class ModelEstudianteTestCase(TestCase):
    # def test_falla(self):
        # self.fail('Test Fallido :C')
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre ='Test de Modelo',
            email= 'testdemodelo@gmail.com',
            dni='1234567891p',
            fecha_nacimiento ='2023-02-02',
            movil='123456789',
        )
        
    def test_verifica_atributos_de_estudiante(self):
        '''Test que verifica los atributos del modelo de Estudiante'''
        self.assertEqual(self.estudiante.nombre,'Test de Modelo')
        self.assertEqual(self.estudiante.email,'testdemodelo@gmail.com')
        self.assertEqual(self.estudiante.dni,'1234567891p')
        self.assertEqual(self.estudiante.fecha_nacimiento,'2023-02-02')
        self.assertEqual(self.estudiante.movil,'123456789')
       
