from django.urls import path
from .views import *

urlpatterns = [
    path('curso/', curso),
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
]