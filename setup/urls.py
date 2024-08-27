
from django.contrib import admin
from django.urls import path
from instituto.views import estudiantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('estudiantes/', estudiantes)
]
