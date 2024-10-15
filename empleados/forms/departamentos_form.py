from django import forms
from ..models.departamentos import Departamento

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreDepartamento' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionDepartamento',
                'rows': 5
            })
        }
