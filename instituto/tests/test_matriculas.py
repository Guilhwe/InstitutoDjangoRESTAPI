from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Matricula, Estudiante,Curso




class MatriculasTestCase(APITestCase):
    fixtures =['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='willy')
        self.url = reverse('Matricula-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudiante =Estudiante.objects.get(pk=1)
        
        self.curso = Curso.objects.get(pk=1)
        
        self.matricula= Matricula.objects.get(pk=1)
        
    
    def test_requisicion_post_para_crear_matricula(self):
        '''Test para verificar la requisicion POST para crear una matrícula'''
        datos ={
            'estudiante': self.estudiante.pk,
            'curso': self.curso.pk,
            'turno': 'M'
        }
        response = self.client.post(self.url, data=datos)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicion_para_deletear_un_CURSO(self):
        '''Test de requisicion DELETE un CURSO '''
        
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicion_put_para_actualizar_una_matricula(self):
        '''Test de requisicion PUT para una matricula'''
        datos={
            'estudiante': self.estudiante.pk,
            'curso': self.curso.pk,
            'turno': 'M'


        }
        response = self.client.put(f'{self.url}1/', data=datos)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)