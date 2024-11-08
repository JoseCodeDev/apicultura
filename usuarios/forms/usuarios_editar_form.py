from django import forms
from django.contrib.auth.models import User

class UsuariosEditarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'is_staff': 'Es administrador',
            'is_active': 'Activo',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-4',
                'id': 'nickname',
                'type': 'text',
                'maxlength': 150,
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control mb-4',
                'id': 'nombresUsuario',
                'type': 'text',
                'maxlength': 150,
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control mb-4',
                'id': 'apellidosUsuario',
                'type': 'text',
                'maxlength': 150,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-4',
                'id': 'emailUsuario',
                'type': 'email',
                'maxlength': 254,
            }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'form-check-input mb-4',
                'id': 'isStaffUsuario',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input mb-4',
                'id': 'isActiveUsuario',
            }),
        }
    