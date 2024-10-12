from django import forms
from ..models import Categoria


class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nombreCategoria' 
            })
        }