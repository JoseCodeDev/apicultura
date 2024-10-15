from django import forms
from ..models.puestos import Puesto

class PuestosForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombrePuesto' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionPuesto',
                'rows': 5
            })
        }
