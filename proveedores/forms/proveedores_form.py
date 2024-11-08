from django import forms
from ..models.proveedores import Proveedor

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'rfc', 'direccion', 'telefono_empresa', 'email_empresa', 'tipo_persona', 'banco', 'numero_cuenta', 'representante_nombres', 'representante_apellidos', 'representante_sexo', 'representante_telefono', 'representante_email', 'activo',]
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
            'direccion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'direccionEmpresaProveedor',
                'rows': 5,
                'type': 'textarea',
            }),
            'telefono_empresa': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'telefonoEmpresaProveedor',
                'type': 'number',
                'maxlength': 12,
            }),
            'email_empresa': forms.EmailInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'emailEmpresaProveedor',
                'type': 'email',
                'maxlength': 50,
            }),
            'tipo_persona': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'tipoPersonaProveedor' ,
                'type': 'select',
                'maxlength': 6,
            }),
            'banco': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'bancoEmpresaProveedor' ,
                'type': 'text',
                'maxlength': 100,
            }),
            'numero_cuenta': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'numeroCuentaEmpresaProveedor' ,
                'type': 'number',
                'maxlength': 18,
            }),
            'representante_nombres': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'representanteNombresProveedor',
                'type': 'text',
                'maxlength': 50,
            }),
            'representante_apellidos': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                    'id': 'representanteApellidosProveedor',
                'type': 'text',
                'maxlength': 50,
            }),
            'representante_sexo': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'representanteSexoProveedor',
                'type': 'date',
                'maxlength': 9,
            }),
            'representante_telefono': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'representanteTelefonoProveedor',
                'type': 'number',
                'maxlength': 10,
            }),
            'representante_email': forms.EmailInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'representanteEmailProveedor',
                'type': 'email',
                'maxlength': 50,
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'activoProveedor' 
            }),
        }
