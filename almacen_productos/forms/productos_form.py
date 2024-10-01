from django import forms
from ..models import Categoria, Producto

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreProducto' 
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockProducto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'categoriaProducto' 
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecciona una categoría"
