from django import forms
from cdap.models import Persona, Locacion, Empresa

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

class LocacionForm(forms.ModelForm):
    class Meta:
        model = Locacion
        fields = [
            'nombre',
            'comentario',
            'activo',
        ]
        labels = {
            'nombre': 'Nombre',
            'comentario': 'Comentario',
            'activo': 'Activo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'responsable',
            'email',
            'comentario',
            'activo',
            'locacion',
        ]
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'responsable': 'Responsable',
            'email': 'Email',
            'comentario': 'Comentario',
            'activo': 'Activo',
            'locacion': 'Locacion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'locacion': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
