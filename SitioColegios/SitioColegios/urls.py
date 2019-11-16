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
from SitioColegios.views import SchoolList, SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate
#from SitioColegios.views import index, school_delete, school_editar, school_listar, evaluar, galeria, index, school_view, SchoolList, \
 #   SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate
from . import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls) ),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Vista estatica del index
    path('galeria/', views.galeria, name='galeria'),
    path('evaluar/', RatingsCreate.as_view(), name='crear_evaluacion'),
    path('listar/', SchoolList.as_view(), name='school_listar'),
    #url(r'^editar/(?P<pk>\d+)/$', views.school_listar, name='school_listar'),
    # url(r'^editar/(?P<id_School>\d+)/$', views.school_editar, name='school_editar'),
    path('editar/<pk>', SchoolUpdate.as_view(), name='school_editar'),
    path('nuevo/', SchoolCreate.as_view(), name='school_view'),
    path('eliminar/<pk>', SchoolDelete.as_view(), name='school_delete'),
    #path ('catalog/', include('catalog.urls')), #aplicacion de catalogo de colegios.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)