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


#Importamos los modelos de la Base de datos.

from catalog.models import SchoolType, state_province, School, Ratings
from catalog.forms import SchoolForm, RatingsForm, RegistroForm, FormLogin, ContactForm

# def index(request):
#      School_instance = School.objects.all().order_by('Name')
#      loop_range = range (1,6)
#      contexto = {'School_instance':School_instance, 'loop_range': loop_range}
#      return render(
#           request,
#           'home/index.html',
#           contexto,
#      )


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


class IndexList(ListView):
     model = School
     queryset = School.objects.all().order_by('Name')
     template_name = 'home/index.html'
     paginate_by = 4


class SchoolList(ListView):
     model = School
     list_filter = ('Name', 'Score', 'State_Province', 'Type')
     queryset = School.objects.all().order_by('Name')
     template_name = 'admin/school_list.html'
     paginate_by = 4


class SchoolCreate( CreateView):

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
     form_class = RatingsForm
     template_name = 'evaluar/evaluacion.html'
     success_url = reverse_lazy('index')

class Galeria(ListView):
     model = School
     template_name = 'galeria/galeria.html'
     paginate_by = 6

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

def contact(request):
     return render(
     request,
     'contact/contacto.html',
     context={},
)

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

     def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)



# def logout(request):

#     do_logout(request)
#     # Redireccionamos a la portada
#     return redirect('/')

# Creacion de vistas para Usuarios.

# def register(request):
#     # Creamos el formulario de autenticación vacío
#     form = UserCreationForm()
#     if request.method == "POST":
#         # Añadimos los datos recibidos al formulario
#         form = UserCreationForm(data=request.POST)
#         # Si el formulario es válido...
#         if form.is_valid():

#             # Creamos la nueva cuenta de usuario
#             user = form.save()

#             # Si el usuario se crea correctamente 
#             if user is not None:
#                 # Hacemos el login manualmente
#                 do_login(request, user)
#                 # Y le redireccionamos a la portada
#                 return redirect('/')

#     # Si llegamos al final renderizamos el formulario
#     return render(request, "users/register.html", {'form': form})

# def login(request):
#     # Creamos el formulario de autenticación vacío
#     form = AuthenticationForm()
#     if request.method == "POST":
#         # Añadimos los datos recibidos al formulario
#         form = AuthenticationForm(data=request.POST)
#         # Si el formulario es válido...
#         if form.is_valid():
#             # Recuperamos las credenciales validadas
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             # Verificamos las credenciales del usuario
#             user = authenticate(username=username, password=password)

#             # Si existe un usuario con ese nombre y contraseña
#             if user is not None:
#                 # Hacemos el login manualmente
#                 do_login(request, user)
#                 # Y le redireccionamos a la portada
#                 return redirect('/')

#     # Si llegamos al final renderizamos el formulario
#     return render(request, "users/login.html", {'form': form})

