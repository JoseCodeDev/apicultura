from django import forms
from ..models.pedidos import Pedido
from proveedores.models import Proveedor

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['proveedor', 'estado', 'fecha_entrega', 'observaciones']
        widgets = {
            'proveedor': forms.Select(attrs={
                'class': 'form-control mb-4',
                'id': 'proveedorSelect'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control mb-4',
                'id': 'estadoSelect'
            }),
            'fecha_entrega': forms.DateInput(attrs={
                'class': 'form-control mb-4',
                'type': 'date'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control mb-4',
                'rows': 3
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proveedor'].queryset = Proveedor.objects.filter(activo=True)
        self.fields['proveedor'].empty_label = "Selecciona un proveedor"
