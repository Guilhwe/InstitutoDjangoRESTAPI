
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')

    def test_autentificacion_user_con_credenciales_correctas(self):
        '''Test que verifica la autentificacion de un user con las credenciales correctas'''
        usuario= authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
    
    def test_autentificacion_user_con_credenciales_incorrectas(self):
        '''Test que verifica la autentificacion de un username credenciales incorrectas'''
        usuario= authenticate(username='admn', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
    
    def test_autentificacion_user_con_credenciales_incorrectas(self):
        '''Test que verifica la autentificacion de un user con contraseña credenciales incorrectas'''
        usuario= authenticate(username='admin', password='admn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)