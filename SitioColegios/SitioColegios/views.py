from catalog.models import SchoolType, User, state_province, School, Ratings
from django.http import  HttpResponse 
from django.template import Template, Context
from django.shortcuts import render


def index(request):
     #doc_externo=open("/Users/juanshocl/Documents/GitHub/SitioColegios/SitioColegios/templates/home/index.html")
     # plt_index = Template(doc_externo.read())      
     # doc_externo.close()
     # contexto  = Context()
     # documento= plt_index.render(contexto)
     # return HttpResponse(documento)
     return render(
          request,
          'index.html',
          context={},
     )


def galeria(request):
     # doc_galeria = open("/Users/juanshocl/Documents/GitHub/SitioColegios/SitioColegios/templates/galeria/galeria.html")
     # plt_galeria = Template(doc_galeria.read())
     # doc_galeria.close()
     # return HttpResponse(plt_galeria.render(Context())) 
     return render(
     request,
     'galeria/galeria.html',
     context={},
)

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")