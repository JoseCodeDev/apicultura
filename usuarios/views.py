from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms.usuarios_crear_form import UsuariosCrearForm
from .forms.usuarios_editar_form import UsuariosEditarForm
from .forms.usuarios_cambio_contrasenia_form import UsuariosCambioContreseniaForm

# Muestra la lista de usuarios
def mostrar(request):
    usuarios = User.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})


# Agrega un nuevo usuario
def agregar(request):
    if request.method == 'GET':
        return render(request, 'agregar.html', {'form': UsuariosCrearForm()})
    elif request.method == 'POST':
        form = UsuariosCrearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario agregado exitosamente.')
            return redirect('usuarios_mostrar')
        else:
            messages.error(request, 'Datos no válidos del formulario.')
            return render(request, 'agregar.html', {'form': form})


# Edita un usuario existente
def editar(request, id_usuario):
    usuario = get_object_or_404(User, pk=id_usuario)
    
    if request.method == 'GET':
        form = UsuariosEditarForm(instance=usuario)
        return render(request, 'editar.html', {'usuario': usuario, 'form': form})
    elif request.method == 'POST':
        form = UsuariosEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario editado exitosamente.')
            return redirect('usuarios_mostrar')
        else:
            messages.error(request, 'Datos no válidos del formulario.')
            return render(request, 'editar.html', {'usuario': usuario, 'form': form})


# @login_required
def cambiar_contrasenia(request, id_usuario):
    usuario = get_object_or_404(User, pk=id_usuario)
    
    # Verificar que el usuario actual tenga permiso para cambiar la contraseña (opcional)
    # if not request.user.is_staff and request.user != usuario:
    #     messages.error(request, 'No tienes permiso para cambiar la contraseña de este usuario.')
    #     return redirect('usuarios_mostrar')
    
    if request.method == 'GET':
        form = UsuariosCambioContreseniaForm(user=usuario)
        return render(request, 'cambioContrasenia.html', {'usuario': usuario, 'form': form})
    elif request.method == 'POST':
        form = UsuariosCambioContreseniaForm(user=usuario, data=request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva contraseña
            # update_session_auth_hash(request, usuario)  # Mantiene al usuario autenticado después del cambio
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('usuarios_mostrar')
        else:
            messages.error(request, 'Datos no válidos del formulario.')
            return render(request, 'cambioContrasenia.html', {'usuario': usuario, 'form': form})


# Elimina un usuario existente
def eliminar(request, id_usuario):
    usuario = get_object_or_404(User, pk=id_usuario)
    
    if request.method == 'GET':
        form = UsuariosCrearForm(instance=usuario)
        
        # Marcar todos los campos como readonly
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'eliminar.html', {'usuario': usuario, 'form': form})
    elif request.method == 'POST':
        try:
            usuario.delete()
            messages.success(request, 'Usuario eliminado exitosamente.')
            return redirect('usuarios_mostrar')
        except Exception:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'eliminar.html', {'usuario': usuario, 'form': form})
