from rest_framework import serializers
from instituto.models import Estudiante,Curso

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estudiante
        fields = ['id','nombre','email','dni','fecha_nacimiento','movil']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields = '__all__'