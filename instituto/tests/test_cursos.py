from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Curso
from instituto.serializers import CursoSerializer


class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Curso-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso= Curso.objects.create(
            codigo='CTT',
            descripcion='EJEMPLO',
            nivel='A'
        )

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
        