from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Django", comision=93233)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)