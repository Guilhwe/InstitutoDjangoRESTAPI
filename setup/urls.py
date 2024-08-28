
from django.contrib import admin
from django.urls import include, path
from instituto.views import EstudianteViewSet, CursoViewSet,MatriculaViewSet,ListaMatriculaEstudiante,ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudiantes', EstudianteViewSet, basename='Estudiante')
router.register('Cursos', CursoViewSet,basename='Curso')
router.register('matriculas', MatriculaViewSet,basename='Matricula')
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include (router.urls)),
    path('estudiantes/<int:pk>/matriculas/',ListaMatriculaEstudiante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
]
