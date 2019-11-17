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
from django.contrib.auth.views import login
from SitioColegios.views import SchoolList, SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate, contact, Galeria, IndexList, RegisterUsuario
#from SitioColegios.views import index, school_delete, school_editar, school_listar, evaluar, galeria, index, school_view, SchoolList, \
 #   SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexList.as_view(), name='index'), #Vista estatica del index
    path('galeria/', Galeria.as_view(), name='galeria'),
    path('contacto/', views.contact, name='contact'),
    path('evaluar/', RatingsCreate.as_view(), name='crear_evaluacion'),
    path('listar/', SchoolList.as_view(), name='school_listar'),
    path('editar/<pk>', SchoolUpdate.as_view(), name='school_editar'),
    path('nuevo/', SchoolCreate.as_view(), name='school_crear'),
    path('eliminar/<pk>', SchoolDelete.as_view(), name='school_delete'),
    path('register/',RegisterUsuario.as_view(), name='registrar'),
    path('login/', login,{'template_name': 'index.html'}, name='login'),
    path('logout/', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)