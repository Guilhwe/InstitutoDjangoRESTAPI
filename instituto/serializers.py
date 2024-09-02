from rest_framework import serializers
from instituto.models import Estudiante,Curso,Matricula
from instituto.validators import dni_invalido, movil_invalido, nombre_invalido

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estudiante
        fields = '__all__'
    def validate(self,datos):
        if dni_invalido(datos['dni']):
              raise serializers.ValidationError({'dni':'El dni debe tener 10 numeros y una letra al final'})
        if nombre_invalido(datos['nombre']):
              raise serializers.ValidationError({'nombre':'EL NOMBRE SOLO PUEDE CONTENER LETRAS'})
        if movil_invalido(datos['movil']):
              raise serializers.ValidationError({'movil':'El numero de telefono tiene que tener 9 numeros'})
        return datos
        

   

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Matricula
            exclude =[]

class ListaMatriculasEstudianteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descripcion')
    turno= serializers.SerializerMethodField()
    class Meta:
          model = Matricula
          fields = ['curso','turno']
    def get_turno(self,obj):
        return obj.get_turno_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
     estudiante_nombre = serializers.ReadOnlyField(source = 'estudiante.nombre')
     class Meta:
          model = Matricula
          fields = ['estudiante_nombre']