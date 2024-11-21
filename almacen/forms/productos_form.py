from django import forms
from ..models.productos import Producto
from ..models.insumos import Insumo
from ..models.categorias import Categoria

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'categoria', 'stock_minimo', 'stock_actual', 'iva', 'ganancia', 'costo_promedio', 'precio_venta', 'activo']
        widgets = {
            'sku': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'skuProducto',
                'maxlength': 12
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreProducto' 
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionProducto',
                'rows': 5
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'categoriaProducto' 
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockMinimoProducto'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockActualProducto'
            }),
            'iva': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'ivaProducto'
            }),
            'ganancia': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'gananciaProducto'
            }),
            'costo_promedio': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'costoPromedioProducto'
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'precioVentaProducto'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'activoProducto' 
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='producto', activo=True)
        self.fields['categoria'].empty_label = "Selecciona una categoría"
        self.fields['stock_actual'].widget.attrs['readonly'] = True
        self.fields['costo_promedio'].widget.attrs['readonly'] = True
        self.fields['precio_venta'].widget.attrs['readonly'] = True
    
    def clean_sku(self): 
        sku = self.cleaned_data.get('sku') 
        instance = self.instance
        
        if not (8 <= len(sku) <= 12): 
            raise forms.ValidationError('El SKU del producto debe tener entre 8 y 12 caracteres.') 
        
        if (Producto.objects.filter(sku=sku).exclude(pk=instance.pk).exists() or Insumo.objects.filter(sku=sku).exists()): 
            raise forms.ValidationError('El SKU ya existe en productos o insumos. Por favor, ingrese un SKU único.') 
        return sku

    def clean_descripcion(self): 
        descripcion = self.cleaned_data.get('descripcion') 
        if not descripcion: 
            return 'Sin descripción' 
        return descripcion
