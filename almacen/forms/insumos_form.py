from django import forms
from ..models.insumos import Insumo
from ..models.categorias import Categoria
from ..models.productos import Producto

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['sku', 'nombre', 'descripcion', 'stock_minimo', 'stock_actual', 'categoria']
        widgets = {
            'sku': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'skuInsumo',
                'maxlength': 12
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreInsumo',
                'maxlength': 50
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'descripcionInsumo',
                'rows': 5
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockMinimoInsumo'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'stockActualInsumo'
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
        self.fields['stock_actual'].widget.attrs['readonly'] = True
    
    def clean_sku(self): 
        sku = self.cleaned_data.get('sku') 
        instance = self.instance
        
        if not (8 <= len(sku) <= 12): 
            raise forms.ValidationError('El SKU del insumo debe tener entre 8 y 12 caracteres.') 
        
        if (Insumo.objects.filter(sku=sku).exclude(pk=instance.pk).exists() or Producto.objects.filter(sku=sku).exists()):
            raise forms.ValidationError('El SKU ya existe  en productos o insumos. Por favor, ingrese un SKU único.') 
        return sku
        
    def clean_descripcion(self): 
        descripcion = self.cleaned_data.get('descripcion') 
        if not descripcion: 
            return 'Sin descripción' 
        return descripcion
    
    def clean_categoria(self): 
        categoria = self.cleaned_data.get('categoria')
        
        if not categoria: 
            raise forms.ValidationError('Debe seleccionar una categoría.') 
        
        if not Categoria.objects.filter(pk=categoria.pk, tipo='insumo', activo=True).exists(): 
            raise forms.ValidationError('La categoría seleccionada no es válida.') 
        return categoria

    def clean_categoria(self): 
        categoria = self.cleaned_data.get('categoria')
        
        if not categoria: 
            raise forms.ValidationError('Debe seleccionar una categoría.') 
        
        if not Categoria.objects.filter(pk=categoria.pk, tipo='insumo', activo=True).exists(): 
            raise forms.ValidationError('La categoría seleccionada no es válida.') 
        return categoria
