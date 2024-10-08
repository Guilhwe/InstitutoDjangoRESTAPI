from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Curso
from instituto.serializers import CursoSerializer


class CursosTestCase(APITestCase):
    fixtures =['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='willy')
        self.url = reverse('Curso-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01= Curso.objects.get(pk=1)
        self.curso_02= Curso.objects.get(pk=2)
        

    def test_requisicion_get_para_listar_cursos(self):
        '''Test de requisicion GET'''
        response = self.client.get(self.url)#/cursos/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicion_get_para_un_curso(self):
        '''Test para verificar la requisicion GET para listar un curso'''
        response=self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        datos_curso=Curso.objects.get(pk=1)
        datos_curso_serializados = CursoSerializer(instance=datos_curso).data
        self.assertEqual(response.data, datos_curso_serializados)

    def test_requisicion_post_para_crear_un_curso(self):
        '''Test de requisicion POST para un curso'''
        datos={
            'nivel':'B',
            'codigo':'test',
            'descripcion':'descripcion',
           
        }
        response = self.client.post(self.url,data=datos)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    
    def test_requisicion_para_deletear_un_CURSO(self):
        '''Test de requisicion DELETE un CURSO '''
        
        response = self.client.delete(f'{self.url}1/')#/curso/2/
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    
    def test_requisicion_put_para_actualizar_un_curso(self):
        '''Test de requisicion PUT para un curso'''
        datos={
            'codigo':'CTT',
            'nivel':'A',
            'descripcion':'ejemplo'


        }
        response = self.client.put(f'{self.url}1/', data=datos)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
