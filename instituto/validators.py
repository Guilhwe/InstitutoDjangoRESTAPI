import re
def dni_invalido(dni):
        modelo = '[0-9]{10}[a-z]{1}'
        respuesta = re.findall(modelo,dni)
        return not respuesta
def nombre_invalido(nombre):
        return not nombre.isalpha()
def movil_invalido(movil):
        modelo = '[0-9]{9}'
        respuesta = re.findall(modelo,movil)
        return not respuesta








