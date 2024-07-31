from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicial(request):
    return render(request, 'hello.html')

def curso(self):
    curso = curso(nombre="Desarrollo Web", camada="29")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def profesores(request):

    return HttpResponse('vista profesores')

def estudiantes(request):
    
    return HttpResponse('vista estudiantes')

def entregables(request):
    
    return HttpResponse('vista entregables')