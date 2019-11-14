from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render, redirect

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
def school_list(request):
     School_instance = School.objects.all().order_by('Name')
     loop_range = range (1,6)
     contexto = {'School_instance':School_instance, 'loop_range': loop_range}
     return render(
          request,
          'admin/school_list.html',
          contexto,
     )

def school_edit(request, id_School):
     School_instance = School.objects.get(Id=id_School)
     if request.method == 'GET':
          form =  SchoolForm(instance=School_instance)
     else:
          form = SchoolForm(request.POST, instance=School_instance)
          if form.is_valid():
               form.save()
               return redirect('school_list')
     return render(request, 'admin/school_save.html', {'form':form})

def formulario(request):
    return HttpResponse("Contacto")

# def school_view(request):
#      if request.method == 'POST':
#           form = SchoolForm(request.POST)
#      if form.is_valid():
#           form.save()
#           return redirect('index')
#      else:
#           form = SchoolForm()

#      return render(
#      request,
#      'admin/school_form.html',
#      context={'form': form},
#      )

def school_view(request):
     if request.method == 'POST':
          form = SchoolForm(request.POST)
          if form.is_valid():
               form.save()
          return redirect('index')
     else:
          form = SchoolForm()
          
     return render(
          request,
          'admin/school_form.html', 
          {'form':form})