from django import forms

from catalog.models import School, Ratings

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
        