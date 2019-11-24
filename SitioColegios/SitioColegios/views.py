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
from catalog.serializers import SchoolSerializer, UserSerializer, ContactSerializer


#Importamos los modelos de la Base de datos.

from catalog.models import SchoolType, state_province, School, Ratings, state_province, SchoolType, ContactModel
from catalog.forms import SchoolForm, RatingsForm, RegistroForm, FormLogin, ContactForm,\
      ComunaForm, TypeForm
from catalog.filters import SchooFilter

class IndexList(ListView):
     model = School
     queryset = School.objects.all().order_by('Name')
     template_name = 'home/index.html'
     paginate_by = 4


class SchoolList(ListView):
     model = School
     queryset = School.objects.all().order_by('Name')
     template_name = 'admin/school_list.html'
     paginate_by = 4


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
     model = School
     template_name = 'galeria/galeria.html'
     paginate_by = 6

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

def contact(request):
         return render(
     request,
     'contact/contacto_old.html',
     context={},
)


     # model = Ratings
     # model_shool = School
     # form_class = RatingsForm
     # # second_form_class = SchoolForm
     # #dato = form_class.Score
     # template_name = 'evaluar/evaluacion_list.html'
     # success_url  = reverse_lazy('index')

     # # def get_context_data(self, **kwargs):
     # #      context = super(RatingsCreate, self).get_context_data(**kwargs)
     # #      if 'form' not in context:
     # #           context['form'] = self.form_class(self.request.GET)
     # #      if 'form2' not in context:
     # #           context['form2'] = self.form_class(self.request.GET)
     # #      return context
     
     # # def post(self, request, **args, **kwargs):
     # #      self.object = self.get_object
     # #      form = self.form_class(request.POST)
     # #      form2 = self.second_form_class(request.POST)

# class Contact()

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


#     serializer = SchoolSerializer
#     def get(self, request, format=None):
#          listar  = School.objects.all().order_by('Name')
#          response = self.serializer(listar, many=True)
#          return HttpResponse(json.dumps(response.data), content_type='application/json')


class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all().order_by('-date_joined')
     serializer_class = UserSerializer
     # serializer = UserSerializer
     
     # def get(self, request, format=None):
     #      queryset = User.objects.all().order_by('-date_joined')
     #      response = self.serializer(queryset, many=True, context=self.context).data
     #      return HttpResponse(json.dumps(response.data), content_type='application/json')
    

class ContactViewSet(viewsets.ModelViewSet):
     queryset = ContactModel.objects.all().order_by('Nombre')
     serializer_class = ContactSerializer
     
     # serializer = ContactSerializer

     # def get(self, request, format=None):
     #      queryset = ContactModel.objects.all().order_by('Nombre')
     #      response = self.serializer(queryset, many=True)
     #      return HttpResponse(json.dumps(response.data), content_type='application/json')