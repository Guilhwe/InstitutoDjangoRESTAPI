import re
def dni_invalido(dni):
        return len(dni) != 11
def nombre_invalido(nombre):
        return not nombre.isalpha()
def movil_invalido(movil):
        modelo = '[0-9]{9}'
        respuesta = re.findall(modelo,movil)
        return not respuesta








