from django import forms
from ..models.insumos import Insumo
from ..models.categorias import Categoria

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'stock', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreInsumo' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionInsumo',
                'rows': 5
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockInsumo'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'categoriaInsumo' 
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(InsumosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='insumo', activo=True)
        self.fields['categoria'].empty_label = "Selecciona una categoría"
