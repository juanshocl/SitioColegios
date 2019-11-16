from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.db.models import Avg

from catalog.models import SchoolType, User, state_province, School, Ratings
from catalog.forms import SchoolForm, RatingsForm

def index(request):
     School_instance = School.objects.all().order_by('Name')
     loop_range = range (1,6)
     contexto = {'School_instance':School_instance, 'loop_range': loop_range}
     return render(
          request,
          'home/index.html',
          contexto,
     )


def galeria(request):
     return render(
     request,
     'galeria/galeria.html',
     context={},
)
def school_listar(request):
     School_instance = School.objects.all().order_by('Name')
     loop_range = range (1,6)
     contexto = {'School_instance':School_instance, 'loop_range': loop_range}
     return render(
          request,
          'admin/school_list.html',
          contexto,
     )

def school_editar(request, id_School):
     School_instance = School.objects.get(Id=id_School)
     if request.method == 'GET':
          form = SchoolForm(instance=School_instance)
     else:
          form = SchoolForm(request.POST, instance=School_instance)
          if form.is_valid():
               form.save(request.POST, request.FILES)
          return redirect('school_listar')
     return render(request, 'admin/school_form.html', {'form':form})

def formulario(request):
    return HttpResponse("Contacto")

def evaluar(request):
     if request.method == 'POST':
          form = RatingsForm(request.POST)
        #  rtg = Ratings.objects.all()
          if form.is_valid():
             #  score = form.save(commit=False)
               # valor = Ratings.objects.get(Schools='2cc99d7c-aae5-4c8e-b201-0c309b1bb9d4').Name
               # promedio = Ratings.objects.filter(Schools=score.Id).aggregate(Avg('Score'))
               # suma = Ratings.objects.filter(Id=)
               # Ratings.objects.filter(Id=).aggregate(Avg('Score'))
               # Author.objects.values('name').annotate(average_rating=Avg('book__rating'))
               # for rat in rtg:
               #      if rat.Schools == form.Schools:
               #           suma = sum + rat.Score
               #           cont = cont +1
               #      pass
               # prom = suma / cont
               # School.objects.filter(Id=form.Id).Score = prom
               # School.save()
               form.save()

          return redirect('index')
     else:
          form = RatingsForm()

     return render(
     request,
     'evaluar/evaluacion.html',
     context={'form': form},
)
def school_view(request):
     if request.method == 'POST':
          form = SchoolForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()

          return redirect('index')
     else:
          form = SchoolForm()

     return render(
     request,
     'admin/school_form.html', 
     context={'form': form},
     )

def school_delete(request, id_school):
     colegio = School.objects.get(Id=id_school)
     if request.method == 'POST':
          colegio.delete()
          return redirect('school_listar')
     return render(request, 'admin/school_list.html', {'colegio': colegio})