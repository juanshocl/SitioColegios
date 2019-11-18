from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from catalog.models import School, Ratings, ContactModel

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School

        fields = [
            'Name',
            # 'Score',
            'ImageMD',
            'ImageProfile',
            'Address',
            'State_Province',
            'Phone',
            'Type',
            'Review',
        ]
        labels = {
            'Name': 'Nombre',
            # 'Score': 'Valoracion',
            'ImageMD': 'Imagen Grande',
            'ImageProfile': 'Imagen Perfil',
            'Address': 'Dirección',
            'State_Province': 'Comuna',
            'Phone':'Telefono',
            'Type':'Tipo establecimiento',
            'Review': 'Reseña',
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            # 'Score': forms.TextInput(attrs={'class':'form-control'}),
            'ImageMD': forms.FileInput(attrs={'class':'form-control'}),
            'ImageProfile': forms.FileInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'State_Province': forms.Select(attrs={'class':'form-control'}),
            'Phone': forms.TextInput(attrs={'class':'form-control'}),
            'Type': forms.Select(attrs={'class':'form-control'}),
            'Review': forms.Textarea(attrs={'class':'form-control'}),
        }
class RatingsForm(forms.ModelForm):
    
    class Meta:
        model = Ratings

        fields = [
            'User',
            'Score',
            'Schools',
        ]
        labels = {
            'User': 'Usuario',
            'Score': 'Evaluacion',
            'Schools': 'Colegio',
        }
        widgets = {
            'User': forms.Select(attrs={'class':'form-control'}),
            'Score': forms.Select(attrs={'class':'form-control'}),
            'Schools': forms.Select(attrs={'class':'form-control'}),
        }

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields =[
            'username',
            'first_name',
            'last_name',
            'email',
            #'is_superuser',
            'is_staff',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            #'is_superuser': 'Usuario Administrador',
            'is_staff': 'Usuario normal',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repita Password',

        }
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'is_staff': forms.Select(attrs={'class':'form-control'}),
        #     'email': forms.TextInput(attrs={'class':'form-control'}),
        #     'password1': forms.TextInput(attrs={'class':'form-control'}),
        #     'password2': forms.TextInput(attrs={'class':'form-control'}),
        # }


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel

        fields = [
            'Nombre',
            'Email',
            'Rut', 
            'Region',
            'Comuna',
            'Metodo',
            'Msg',
            'Newsletter',
        ]
        labels = {
            'Nombre': 'Nombre',
            'Email': 'Email',
            'Rut': 'Rut', 
            'Region':'Region',
            'Comuna': 'Comuna',
            'Metodo': 'Contacto',
            'Msg': 'Mensaje',
            'Newsletter': 'Newsletter',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'Rut': forms.TextInput(attrs={'class':'form-control'}), 
            'Region': forms.Select(attrs={'class':'form-control'}),
            'Comuna': forms.Select(attrs={'class':'form-control'}),
            'Metodo': forms.Select(attrs={'class':'form-control'}),
            'Msg': forms.Textarea(attrs={'class':'form-control'}),
            'Newsletter': forms.BooleanField(required=False,initial=False,label='News Letter'),

        }

class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
