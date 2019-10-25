from django.http import  HttpResponse

def saludo(request):
     return HttpResponse("Hola que hace") 

def despedida(request):
     return HttpResponse("Adios") 

def ingreso(request):
    return HttpResponse("Ingreso")

def formulario(request):
    return HttpResponse("Contacto")