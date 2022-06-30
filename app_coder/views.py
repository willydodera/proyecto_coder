from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Django", comision=93233)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return HttpResponse('Vista inicio')

def cursos(request):
    return HttpResponse('Vista cursos')

def profesores(request):
    return HttpResponse('Vista profesores')

def entregables(request):
    return HttpResponse('Vista entregables')

def estudiantes(request):
    return HttpResponse('Vista estudiantes')

