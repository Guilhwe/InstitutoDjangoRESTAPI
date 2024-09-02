import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from instituto.models import Estudiante

def generar_dni():
    numero_dni = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    
    
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letra_dni = random.choice(letras)
    
    
    return numero_dni + letra_dni
     
def creando_personas(cantidad_personas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(cantidad_personas):
        dni = generar_dni()
        nombre = fake.name()
        email = '{}@{}'.format(nombre.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        dni = dni
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=30)  
        movil = "{}-{}-{}".format(random.randrange(100, 1000), random.randrange(1000, 10000), random.randrange(10, 100))
        p = Estudiante(nombre=nombre, email=email, dni=dni, fecha_nacimiento=fecha_nacimiento, movil=movil)
        p.save()

creando_personas(50)