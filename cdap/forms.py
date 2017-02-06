from django import forms
from cdap.models import Persona

# formulario para personas
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'documento',
            'foto',
            'activo',
            'empresa',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'documento': 'Documento',
            'foto': 'Foto',
            'activo': 'activo',
            'empresa': 'Empresa',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }
