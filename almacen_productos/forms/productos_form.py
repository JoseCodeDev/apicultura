from django import forms
from ..models import Producto

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_venta', 'categoria', 'stock', 'stock_minimo', 'stock_maximo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreProducto' 
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'precioVentaProducto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'categoriaProducto' 
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockProducto'
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockMinimoProducto'
            }),
            'stock_maximo': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockMaximoProducto'
            }),
            
            
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecciona una categoría"
