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
from SitioColegios.views import index, galeria, evaluar, school_edit, school_list
from . import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls) ),
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'), #Vista estatica del index
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^evaluar$', views.evaluar, name='crear_evaluacion'),
    url(r'^listar$', views.school_list, name='school_list'),
    url(r'^editar/(?P<id_School>\d+)/$', views.school_edit, name='school_editar'),
    url(r'^nuevo', views.school_view, name='school_view'),
    #path ('catalog/', include('catalog.urls')), #aplicacion de catalogo de colegios.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)