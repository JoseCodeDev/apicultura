from django import forms
from ..models.empleados import Empleado

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'direccion', 'telefono', 'grupo_sanguineo', 'fecha_contratacion', 'puesto', 'departamento', 'fecha_alta_ss', 'nss', 'clabe_interbancaria', 'contacto_emergencia_nombres', 'contacto_emergencia_apellidos', 'contacto_emergencia_telefono', 'contacto_emergencia_parentesco', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nombresEmpleado',
                'type': 'text',
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'apellidosEmpleado',
                'type': 'text',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'fechaNacimientoEmpleado',
                'type': 'date',
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'sexoEmpleado',
                'type': 'select',
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control mb-4', 
                'id': 'direccionEmpleado' ,
                'rows': 5,
                'type': 'textarea',
            }),
            'telefono': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'telefonoEmpleado',
                'type': 'number',
            }),
            'grupo_sanguineo': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'grupoSanguineoEmpleado',
                'type': 'select',
            }),
            'fecha_contratacion': forms.DateInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'fechaContratacionEmpleado',
                'type': 'date',
            }),
            'puesto': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'puestoEmpleado',
                'type': 'select',
            }),
            'departamento': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'departamentoEmpleado',
                'type': 'select',
            }),
            'fecha_alta_ss': forms.DateInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'fechaAltaSSEmpleado',
                'type': 'date'
            }),
            'nss': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'nssEmpleado',
                'type': 'number',
            }),
            'clabe_interbancaria': forms.NumberInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'clabeInterbancariaEmpleado',
                'type': 'number',
            }),
            'contacto_emergencia_nombres': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoEmergenciaNombresEmpleado',
                'type': 'text',
            }),
            'contacto_emergencia_apellidos': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoEmergenciaApellidosEmpleado',
                'type': 'text',
            }),
            'contacto_emergencia_telefono': forms.TextInput(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoEmergenciaTelefonoEmpleado',
                'type': 'number',
            }),
            'contacto_emergencia_parentesco': forms.Select(attrs={
                'class': 'form-control mb-4', 
                'id': 'contactoEmergenciaParentescoEmpleado',
                'type': 'select',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'activoEmpleado' 
            }),
        }
