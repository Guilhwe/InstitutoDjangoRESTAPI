from rest_framework import serializers
from instituto.models import Estudiante,Curso,Matricula

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estudiante
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Matricula
            exclude =[]