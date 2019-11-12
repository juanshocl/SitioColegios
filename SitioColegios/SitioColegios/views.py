from catalog.models import SchoolType, User, state_province, School, Ratings
from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render


def index(request):
     # SchooName = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Name
     # imagen_profile = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').ImageProfile
     # imagen_modal = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').ImageMD
     # address = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Address
     # phone = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Phone
     # review = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Review
     # state_province = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').State_Province.NameSP
     # school_type = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Type.Description
     # direccion = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Address
     # rating = School.average_rating
     School_instance = School.objects.all()
     # score = School.objects.get(self. Id=Ratings.Id).Name
     # score = School.objects.get
     score = 3.5 #School.objects.get(Id= 'ab6e52a8-088c-43ea-979d-1698e0f3f66d').Score 
     loop_range = range (1,6)
     return render(
          request,
          'index.html',
          context={'School_instance': School_instance,'score': score,'loop_range': loop_range},
     )


def galeria(request):
     
     return render(
     request,
     'galeria/galeria.html',
     context={},
)

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")