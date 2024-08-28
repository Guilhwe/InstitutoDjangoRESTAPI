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