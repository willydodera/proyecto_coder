from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre="Django", comision=93233)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "app_coder/inicio.html")

def cursos(request):
     return render (request, "app_coder/cursos.html")

def profesores(request):
     return render (request, "app_coder/profesores.html")

def entregables(request):
     return render (request, "app_coder/entregables.html")

def estudiantes(request):
     return render (request, "app_coder/estudiantes.html")

