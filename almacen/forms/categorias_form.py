from django import forms
from ..models.categorias import Categoria

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control  mb-4',
                'id': 'nombreCategoria' 
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'tipoCategoria',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(CategoriasForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].empty_label = "Selecciona un tipo"