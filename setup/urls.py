
from django.contrib import admin
from django.urls import include, path
from instituto.views import EstudianteViewSet, CursoViewSet,MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudiantes', EstudianteViewSet, basename='Estudiante')
router.register('Cursos', CursoViewSet,basename='Curso')
router.register('matriculas', MatriculaViewSet,basename='Matricula')
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include (router.urls)),
]
