from django import forms
from ..models import Cliente

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'genero', 'telefono', 'email', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombresCliente' 
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'apellidosCliente'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'generoCliente'
            }),
            'telefono': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'telefonoCliente'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'emailCliente' 
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',  
                'id': 'activoCliente'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(ClientesForm, self).__init__(*args, **kwargs)
        self.fields['genero'].empty_label = "Selecciona un género"
