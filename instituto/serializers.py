from rest_framework import serializers
from instituto.models import Estudiante,Curso,Matricula

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estudiante
        fields = '__all__'
    def validate_dni(self,dni):
         if len(dni) != 11:
              raise serializers.ValidationError('El dni debe tener 11 digitos')
         return dni
    def validate_nombre(self,nombre):
         if not  nombre.isalpha():
              raise serializers.ValidationError('EL NOMBRE SOLO PUEDE CONTENER LETRAS')
         return nombre
    def validate_movil(self,movil):
         if len(movil) != 9:
              raise serializers.ValidationError('El numero de telefono tiene que tener 9 numeros')
         return movil

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