from catalog.models import SchoolType, User, state_province, School, Ratings
from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render


def index(request):
     SchooName = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Name
     imagen_profile = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').ImageProfile
     imagen_modal = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').ImageMD
     address = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Address
     phone = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Phone
     review = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Review
     state_province = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').State_Province.NameSP
     school_type = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Type.Description
     # direccion = School.objects.get(Id='bbd6a97a-ce81-4368-93ce-eb95dfc90fad').Address
     School_instance = School.objects.all()
     return render(
          request,
          'index.html',
          context={'SchooName': SchooName, 'imagen_modal':imagen_modal, 'imagen_profile': imagen_profile, 'address':address, 'phone': phone, 'review':review, 'state_province':state_province, 'school_type':school_type, 'School_instance': School_instance},
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