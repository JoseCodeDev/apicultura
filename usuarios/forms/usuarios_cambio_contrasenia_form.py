from django.contrib.auth.forms import SetPasswordForm
from django import forms

class UsuariosCambioContreseniaForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-4',
            'id': 'newPassword1Usuario',
            'maxlength': 128,
        })
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-4',
            'id': 'newPassword2Usuario',
            'maxlength': 128,
        })
    )
