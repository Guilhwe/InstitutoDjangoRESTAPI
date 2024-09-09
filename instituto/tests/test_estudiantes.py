from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from instituto.models import Estudiante
from instituto.serializers import EstudianteSerializer


class EstudiantesTestCase(APITestCase):
    fixtures =['prototipo_banco.json']
    def setUp(self):
        # self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.usuario = User.objects.get(username='willy')
        self.url = reverse('Estudiante-list')
        self.client.force_authenticate(user=self.usuario)
        # self.estudiante_01= Estudiante.objects.create(
        #     nombre ='Test estudiante UM',
        #     email = 'testestudiante01@gmail.com',
        #     dni= '1234567892e',
        #     fecha_nacimiento='2024-01-02',
        #     movil = '634634634',
        # )
        self.estudiante_01 = Estudiante.objects.get(pk=1)
        self.estudiante_02 = Estudiante.objects.get(pk=2)
        # self.estudiante_02= Estudiante.objects.create(
        #     nombre ='Test estudiante DOS',
        #     email = 'testestudiante02@gmail.com',
        #     dni= '0987654321r',
        #     fecha_nacimiento='2024-01-02',
        #     movil = '633333333',
        # )
    def test_requisicion_get_para_listar_estudiantes(self):
        '''Test de requisicion GET'''
        response = self.client.get(self.url)#/estudiantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicion_get_para_listar_un_estudiante(self):
        '''Test de requisicion GET para un estudiante'''
        response = self.client.get(self.url+'1/')#/estudiantes/1/ se compara
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        datos_estudiante= Estudiante.objects.get(pk=1)#con los datos del estudiante en el banco de datos
        datos_estudiante_serializados =EstudianteSerializer(datos_estudiante).data
        # print(datos_estudiante_serializados)
        self.assertEqual(response.data,datos_estudiante_serializados)

    def test_requisicion_post_para_crear_un_estudiante(self):
        '''Test de requisicion POST para un estudiante'''
        datos={
            'nombre':'test',
            'email':'test@gmail.com',
            'dni':'0987654321u',
            'fecha_nacimiento' : '2003-03-27',
            'movil':'543654234',

        }
        response = self.client.post(self.url,datos)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_requisicion_para_deletear_un_estudiante(self):
        '''Test de requisicion DELETE un estudiante'''
        
        response = self.client.delete(f'{self.url}2/')#/estudiante/2/
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicion_put_para_actualizar_un_estudiante(self):
        '''Test de requisicion PUT para un estudiante'''
        datos={
            'nombre':'test',
            'email':'test@gmail.com',
            'dni':'0987654321n',
            'fecha_nacimiento' : '2003-03-27',
            'movil':'543654234',

        }
        response = self.client.put(f'{self.url}1/', data=datos)
        self.assertEqual(response.status_code,status.HTTP_200_OK)