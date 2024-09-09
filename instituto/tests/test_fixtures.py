from django.test import TestCase
from instituto.models import Estudiante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carga_de_fixtures(self):
        '''Test que verifica la carga de fixtures'''
        estudiante =Estudiante.objects.get(dni='43352825G')
        curso =Curso.objects.get(pk=1)
        self.assertEqual(estudiante.movil, '319-2923-85')
        self.assertEqual(curso.codigo,'PPT')
