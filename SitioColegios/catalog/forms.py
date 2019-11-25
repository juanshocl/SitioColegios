from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from catalog.models import School, Ratings, ContactModel, state_province, SchoolType

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School

        fields = [
            'Name',
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
            #'User': forms.TextInput(attrs={'class':'form-control'}),
            #'Score': forms.Select(attrs={'class':'form-control'}),
            'Score': forms.Select(attrs={'class': 'form-control'}, choices=(
                (None, 'None'),
                (1, '★☆☆☆☆'),
                (2, '★★☆☆☆'),
                (3, '★★★☆☆'),
                (4, '★★★★☆'),
                (5, '★★★★★')
            )),
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
            'is_staff',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'is_staff': 'Usuario normal',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repita Password',

        }


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

class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

class ComunaForm(forms.ModelForm):
    
    class Meta:
        model = state_province

        fields =[
            'NameSP',
        ]

        labels = {
            'NameSP': 'Comuna',
        }

class TypeForm(forms.ModelForm):
    
    class Meta:
        model = SchoolType
        fields =[
            'Description',
        ]
        labels = {
            'Description': 'Tipo Establecimiento',
        }