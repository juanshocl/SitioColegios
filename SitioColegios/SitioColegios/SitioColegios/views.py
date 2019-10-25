from django.http import  HttpResponse
from django.template import Template, Context

def saludo(request):
     doc_externo=open("/Users/juanshocl/Documents/GitHub/SitioColegios/SitioColegios/SitioColegios/SitioColegios/Templates/index.html")
     plt_index = Template(doc_externo.read())      
     doc_externo.close()
     contexto  = Context()
     documento= plt_index.render(contexto)
     return HttpResponse(documento) 

def despedida(request):
     return HttpResponse("Adios") 

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")