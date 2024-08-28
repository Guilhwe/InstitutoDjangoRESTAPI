from rest_framework import serializers
from instituto.models import Estudiante,Curso,Matricula

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estudiante
        fields = '__all__'
    def validate(self,datos):
        if len(datos['dni']) != 11:
              raise serializers.ValidationError({'dni':'El dni debe tener 11 digitos'})
        if not datos['nombre'].isalpha():
              raise serializers.ValidationError({'nombre':'EL NOMBRE SOLO PUEDE CONTENER LETRAS'})
        if len(datos['movil']) != 9:
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