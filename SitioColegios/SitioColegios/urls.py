"""SitioColegios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from SitioColegios.views import SchoolList, SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate, contact, Galeria, IndexList, RegisterUsuario,\
    Login, LogoutUser
#from SitioColegios.views import index, school_delete, school_editar, school_listar, evaluar, galeria, index, school_view, SchoolList, \
 #   SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls), #OK
    path('', IndexList.as_view(), name='index'), #Vista estatica del index Vista Operativa
    path('galeria/', Galeria.as_view(), name='galeria'), #Funcionando
    path('contacto/', views.contact, name='contact'), #Template listo, Falta vincular el form con la Base de datos.
    path('evaluar/',  login_required(RatingsCreate.as_view()), name='crear_evaluacion'), # Pendiente calculo de evaluacion para almacenar en School
    path('listar/', login_required(SchoolList.as_view()), name='school_listar'), #Listo, funciona Perfecto el CRUD
    path('editar/<pk>', login_required(SchoolUpdate.as_view()), name='school_editar'), #Listo
    path('nuevo/', login_required(SchoolCreate.as_view()), name='school_crear'), #Listo
    path('eliminar/<pk>', login_required(SchoolDelete.as_view()), name='school_delete'), #Listo
    path('register/',RegisterUsuario.as_view(), name='registrar'), #Listo
    path('login/',Login.as_view(), name='Login'),
    #path('logout/', views.logout,{'template_name': 'index.html'}, name='logout'),
    path('logout/', login_required(LogoutUser.as_view()), name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)