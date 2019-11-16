from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import F


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
# def school_listar(request):
#      School_instance = School.objects.all().order_by('Name')
#      loop_range = range (1,6)
#      contexto = {'School_instance':School_instance, 'loop_range': loop_range}
#      return render(
#           request,
#           'admin/school_list.html',
#           contexto,
#      )

# def school_editar(request, id_School):
#      School_instance = School.objects.get(Id=id_School)
#      if request.method == 'GET':
#           form = SchoolForm(instance=School_instance)
#      else:
#           form = SchoolForm(request.POST, instance=School_instance)
#           if form.is_valid():
#                form.save(request.POST, request.FILES)
#           return redirect('school_listar')
#      return render(request, 'admin/school_form.html', {'form':form})

def formulario(request):
    return HttpResponse("Contacto")

# def evaluar(request):
#      if request.method == 'POST':
#           form = RatingsForm(request.POST)
#           if form.is_valid():
#                form.save()
#           return redirect('index')
#      else:
#           form = RatingsForm()

#      return render(
#      request,
#      'evaluar/evaluacion.html',
#      context={'form': form},
# )
# def school_view(request):
#      if request.method == 'POST':
#           form = SchoolForm(request.POST, request.FILES)
#           if form.is_valid():
#                form.save()

#           return redirect('listar')
#      else:
#           form = SchoolForm()

#      return render(
#      request,
#      'admin/school_form.html', 
#      context={'form': form},
#      )

# def school_delete(request, id_School):
#      colegio = School.objects.get(Id=id_School)
#      if request.method == 'POST':
#           colegio.delete()
#           return redirect('school_listar')
#      return render(request, 
#      'admin/school_delete.html',
#       {'colegio': colegio})

class SchoolList(ListView):
     model = School
     template_name = 'admin/school_list.html'

class SchoolCreate(CreateView):
     model = School
     form_class = SchoolForm
     template_name = 'admin/school_form.html'
     success_url = reverse_lazy('school_listar')

class SchoolUpdate(UpdateView):
     model = School
     form_class = SchoolForm
     template_name = 'admin/school_form.html'
     success_url = reverse_lazy('school_listar')
     
class SchoolDelete(DeleteView):
     model = School
     template_name  = 'admin/school_delete.html'
     success_url  = reverse_lazy('school_listar')

class RatingsList(ListView):
     model = Ratings
     template_name = 'evaluar/evaluacion.html'

class RatingsCreate(CreateView):
     model = Ratings
     model_shool = School
     form_class = RatingsForm
     # second_form_class = SchoolForm
     #dato = form_class.Score
     template_name = 'evaluar/evaluacion_list.html'
     success_url  = reverse_lazy('index')

     # def get_context_data(self, **kwargs):
     #      context = super(RatingsCreate, self).get_context_data(**kwargs)
     #      if 'form' not in context:
     #           context['form'] = self.form_class(self.request.GET)
     #      if 'form2' not in context:
     #           context['form2'] = self.form_class(self.request.GET)
     #      return context
     
     # def post(self, request, **args, **kwargs):
     #      self.object = self.get_object
     #      form = self.form_class(request.POST)
     #      form2 = self.second_form_class(request.POST)