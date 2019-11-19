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
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from SitioColegios.views import SchoolList, SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate, Galeria, IndexList, RegisterUsuario,\
    Login, LogoutUser, StateCreate, TypeCreate, ContactCreate, contact
#from SitioColegios.views import index, school_delete, school_editar, school_listar, evaluar, galeria, index, school_view, SchoolList, \
 #   SchoolCreate, SchoolUpdate, SchoolDelete, RatingsCreate
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls), #OK
    path('', IndexList.as_view(), name='index'), #Vista estatica del index Vista Operativa
    path('galeria/', Galeria.as_view(), name='galeria'), #Funcionando
    path('contacto/', ContactCreate.as_view(), name='contact'), #Template listo, Falta vincular el form con la Base de datos.
    path('evaluar/',  login_required(RatingsCreate.as_view()), name='crear_evaluacion'), # Pendiente calculo de evaluacion para almacenar en School
    path('listar/', login_required(SchoolList.as_view()), name='school_listar'), #Listo, funciona Perfecto el CRUD
    path('editar/<pk>', login_required(SchoolUpdate.as_view()), name='school_editar'), #Listo
    path('nuevo/', login_required(SchoolCreate.as_view()), name='school_crear'), #Listo
    path('eliminar/<pk>', login_required(SchoolDelete.as_view()), name='school_delete'), #Listo
    path('register/',RegisterUsuario.as_view(), name='registrar'), #Listo
    path('comuna/',login_required(StateCreate.as_view()) , name='comuna'), #Listo
    path('establecimiento/',login_required(TypeCreate.as_view()), name='establecimiento'), #Listo
    path('accounts/login/',Login.as_view(), name='Login'), #Listo
    path('logout/', login_required(LogoutUser.as_view()), name='logout'), #esta redirigiendo a otra ubicacion.

    path('passreset/password_reset', PasswordResetView.as_view(template_name='passreset/password_reset_form.html', email_template_name="passreset/password_reset_email.html"), name = 'password_reset'), #Listo
    path('passreset/password_reset_done', PasswordResetDoneView.as_view(template_name='passreset/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^passreset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='passreset/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('passreset/done',PasswordResetCompleteView.as_view(template_name='passreset/password_reset_complete.html') , name = 'password_reset_complete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

