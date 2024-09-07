from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Estudiante


class EstudiantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudiante-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudiante_01= Estudiante.objects.create(
            nombre ='Test estudiante UM',
            email = 'testestudiante01@gmail.com',
            dni= '1234567892e',
            fecha_nacimiento='2024-01-02',
            movil = '634634634',
        )
        self.estudiante_02= Estudiante.objects.create(
            nombre ='Test estudiante DOS',
            email = 'testestudiante02@gmail.com',
            dni= '0987654321r',
            fecha_nacimiento='2024-01-02',
            movil = '633333333',
        )
    def test_requisicion_get_para_listar_estudiantes(self):
        '''Test de requisicion GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)