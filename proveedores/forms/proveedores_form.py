from django import forms
from ..models.proveedores import Provedor

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = ['nombre_empresa', 'rfc', 'direccion_fiscal', 'direccion_envio', 'tipo_persona', 'contacto_nombres', 'contacto_apellidos', 'contacto_sexo', 'contacto_telefono', 'contacto_email', 'activo',]
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombreEmpresaProveedor',
                'type': 'text',
                'maxlength': 100,
            }),
            'rfc': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'rfcEmpresaProveedor',
                'type': 'text',
                'maxlength': 13,
            }),
            'direccion_fiscal': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'direccionFiscalEmpresaProveedor',
                'rows': 5,
                'type': 'textarea',
            }),
            'direccion_envio': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'direccionEnviolEmpresaProveedor',
                'rows': 5,
                'type': 'textarea',
            }),
            'tipo_persona': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'tipoPersonaProveedor' ,
                'type': 'select',
                'maxlength': 6,
            }),
            'contacto_nombres': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoNombresProveedor',
                'type': 'text',
                'maxlength': 50,
            }),
            'contacto_apellidos': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoApellidosProveedor',
                'type': 'text',
                'maxlength': 50,
            }),
            'contacto_sexo': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'sexoContactoProveedor',
                'type': 'date',
                'maxlength': 9,
            }),
            'contacto_telefono': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'telefonoContactoProveedor',
                'type': 'number',
                'maxlength': 10,
            }),
            'contacto_email': forms.EmailInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'emailContactoProveedor',
                'type': 'email',
                'maxlength': 50,
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'activoProveedor' 
            }),
        }
