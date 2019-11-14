from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render, redirect

from catalog.models import SchoolType, User, state_province, School, Ratings
from catalog.forms import SchoolForm, RatingsForm

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
     if request.method == 'POST':
          form = RatingsForm(request.POST)
          if form.is_valid():
               
               form.save()
          return redirect('index')
     else:
          form = RatingsForm()

     return render(
     request,
     'evaluar/evaluacion.html',
     context={'form': form},
)

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")