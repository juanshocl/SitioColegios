from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        ]
        labels = {
            'username': 'Nombre Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
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

