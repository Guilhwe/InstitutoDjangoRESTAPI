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

    def test_requisicion_get_para_listar_cursos(self):
        '''Test de requisicion GET'''
        response = self.client.get(self.url)#/cursos/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicion_post_para_crear_un_curso(self):
        '''Test de requisicion POST para un curso'''
        datos={
            'nivel':'B',
            'codigo':'test',
            'descripcion':'descripcion',
           
        }
        response = self.client.post(self.url,datos)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        