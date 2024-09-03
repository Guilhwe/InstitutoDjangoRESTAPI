
from django.contrib import admin
from django.urls import include, path
from instituto.views import EstudianteViewSet, CursoViewSet,MatriculaViewSet,ListaMatriculaEstudiante,ListaMatriculaCurso
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de la  API",
      default_version='v1',
      description="Documentacion de la API Instituto",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('estudiantes', EstudianteViewSet, basename='Estudiante')
router.register('Cursos', CursoViewSet,basename='Curso')
router.register('matriculas', MatriculaViewSet,basename='Matricula')
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include (router.urls)),
    path('estudiantes/<int:pk>/matriculas/',ListaMatriculaEstudiante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


