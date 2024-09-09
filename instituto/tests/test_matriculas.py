from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Matricula, Estudiante,Curso




class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Matricula-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudiante =Estudiante.objects.create(
            nombre= 'EJEMPLO',
            email='ejemplo@email.com',
            dni='123456783p',
            fecha_nacimiento= '1996-02-02',
            movil='879567365'
        )
        self.curso = Curso.objects.create(
            codigo='EJM', 
            descripcion='prueba',
            nivel='A'
        )
        self.matricula= Matricula.objects.create(
            estudiante= self.estudiante,
            curso=self.curso,
            turno='N'
        )
    
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