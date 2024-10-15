from django import forms
from ..models.productos import Producto
from ..models.categorias import Categoria

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio_venta', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreProducto' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionProducto',
                'rows': 5
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockProducto'
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'precioVentaProducto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'categoriaProducto' 
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='producto', activo=True)
        self.fields['categoria'].empty_label = "Selecciona una categoría"
