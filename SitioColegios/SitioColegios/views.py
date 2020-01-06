import json
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, CreateView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

#Importamos los serializers de los modelos.
from catalog.serializers import SchoolSerializer, UserSerializer, ContactSerializer, StateSerializer, TypeSchoolsSerializer


#Importamos los modelos de la Base de datos.

from catalog.models import SchoolType, state_province, School, Ratings, state_province, SchoolType, ContactModel
from catalog.forms import SchoolForm, RatingsForm, RegistroForm, FormLogin, ContactForm,\
      ComunaForm, TypeForm
from catalog.filters import SchooFilter

class IndexList(ListView):
     model = School
     loop_range = range (1,6)
     paginate_by = 2
     template_name = 'home/index.html'

     def get_context_data(self, **kwargs):
          context = super(IndexList,self).get_context_data(**kwargs)
          escuelas = School.objects.all().order_by('Name')
          data = []
          for escuela in escuelas:
               promedio = Ratings.objects.filter(School=escuela.Id).aggregate(Avg('Score'))['Score__avg']
               dic = {
               'Id': escuela.Id,
               'Name' : escuela.Name,
               'Score': promedio,
               'ImageMD':escuela.ImageMD, 
               'ImageProfile':escuela.ImageProfile,
               'Address':escuela.Address,
               'State_Province':escuela.State_Province,
               'Phone':escuela.Phone, 
               'Type':escuela.Type,
               'Review':escuela.Review,
          }
               data.append(dic)

          context['data'] = data
          return context


class SchoolList(ListView):
     loop_range = range (1,6)
     model = School
     template_name = 'admin/school_list.html'
     paginate_by = 4

     def get_context_data(self, **kwargs):
          context = super(SchoolList,self).get_context_data(**kwargs)
          escuelas = School.objects.all().order_by('Name')
          data = []
          for escuela in escuelas:
               promedio = Ratings.objects.filter(Schools=escuela.Id).aggregate(Avg('Score'))['Score__avg']
               dic = {
               'Id': escuela.Id,
               'Name' : escuela.Name,
               'Score': promedio,
               'ImageMD':escuela.ImageMD, 
               'ImageProfile':escuela.ImageProfile,
               'Address':escuela.Address,
               'State_Province':escuela.State_Province,
               'Phone':escuela.Phone, 
               'Type':escuela.Type,
               'Review':escuela.Review,
          }
               data.append(dic)

          context['data'] = data
          return context


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
     template_name = 'evaluar/evaluacion.html'
     form_class = RatingsForm
     success_url = reverse_lazy('index')



class Galeria(ListView):
     loop_range = range (1,6)
     model = School
     template_name = 'galeria/galeria.html'
     paginate_by = 6

     def get_context_data(self, **kwargs):
          context = super(Galeria,self).get_context_data(**kwargs)
          escuelas = School.objects.all().order_by('Name')
          data = []
          for escuela in escuelas:
               promedio = Ratings.objects.filter(Schools=escuela.Id).aggregate(Avg('Score'))['Score__avg']
               dic = {
               'Id': escuela.Id,
               'Name' : escuela.Name,
               'Score': promedio,
               'ImageMD':escuela.ImageMD, 
               'ImageProfile':escuela.ImageProfile,
               'Address':escuela.Address,
               'State_Province':escuela.State_Province,
               'Phone':escuela.Phone, 
               'Type':escuela.Type,
               'Review':escuela.Review,
          }
               data.append(dic)

          context['data'] = data
          return context


class StateCreate(CreateView):
     model = state_province
     form_class = ComunaForm
     template_name = 'admin/state_province.html'
     success_url  = reverse_lazy('school_listar')

class TypeCreate(CreateView):
     model = SchoolType
     form_class = TypeForm
     template_name = 'admin/school_type.html'
     success_url  = reverse_lazy('school_listar')

class ContactCreate(CreateView):
     model = ContactModel
     form_class = ContactForm
     template_name = 'contact/contacto.html'
     success_url  = reverse_lazy('index')



class RegisterUsuario(CreateView):
     model = User
     template_name = 'users/register.html'
     form_class = RegistroForm
     success_url = reverse_lazy('index')

class Login(FormView):
     template_name = 'home/index.html'
     form_class = FormLogin
     success_url = reverse_lazy('index')

     @method_decorator(csrf_protect)
     @method_decorator(never_cache)
     def dispatch(self, request, *args, **kwargs):
          if request.user.is_authenticated:
               return HttpResponseRedirect(self.get_success_url())
          else:
               return super(Login,self).dispatch(request, *args, **kwargs)

     def form_valid(self,form):
          login(self.request, form.get_user())
          return super(Login, self).form_valid(form)
     
class LogoutUser(RedirectView):
     pattern_name = 'logout'
     success_url = reverse_lazy('index')

     def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)

def search(request):
    shools_list = School.objects.all()
    shools_filter = SchooFilter(request.GET, queryset=shools_list)
    return render(request, 'admin/school_list.html', {'filter': shools_filter})

#API
class SchoolViewSet(viewsets.ModelViewSet):
     queryset = School.objects.all().order_by('Name')
     serializer_class = SchoolSerializer

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all().order_by('-date_joined')
     serializer_class = UserSerializer

class ContactViewSet(viewsets.ModelViewSet):
     queryset = ContactModel.objects.all().order_by('Nombre')
     serializer_class = ContactSerializer

class StateViewSet(viewsets.ModelViewSet):
     queryset = state_province.objects.all()
     serializer_class = StateSerializer


class TypeSchoolsViewSet(viewsets.ModelViewSet):
     queryset = SchoolType.objects.all()
     serializer_class = TypeSchoolsSerializer