from django import forms

from catalog.models import School, Ratings

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School

        fields = [
            'Name',
            'Score',
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
            'Score': 'Evaluacion',
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
            'Score': forms.TextInput(attrs={'class':'form-control'}),
            'ImageMD': forms.TextInput(attrs={'class':'form-control'}),
            'ImageProfile': forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'State_Province': forms.Select(attrs={'class':'form-control'}),
            'Phone': forms.TextInput(attrs={'class':'form-control'}),
            'Type': forms.Select(attrs={'class':'form-control'}),
            'Review': forms.TextInput(attrs={'class':'form-control'}),
        }
class RatingsForm(forms.ModelForm):
    
    class Meta:
        model = Ratings

        fields = [
            # Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            'User',
            'Score',
            'Schools',
        ]
        labels = {
            # Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            'User': 'Usuario',
            'Score': 'Evaluacion',
            'Schools': 'Colegio',
        }
        widgets = {
            'User': forms.Select(attrs={'class':'form-control'}),
            'Score': forms.Select(attrs={'class':'form-control'}),
            'Schools': forms.Select(attrs={'class':'form-control'}),

        }
        