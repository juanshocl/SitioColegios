from catalog.models import SchoolType, User, state_province, School, Ratings
from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render


def index(request):
     School_instance = School.objects.all()
     loop_range = range (1,6)
     return render(
          request,
          'index.html',
          context={'School_instance': School_instance,'loop_range': loop_range},
     )


def galeria(request):
     return render(
     request,
     'galeria/galeria.html',
     context={},
)

def evaluar(request):
     return render(
     request,
     'evaluar/evaluacion.html',
     context={},
)

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")