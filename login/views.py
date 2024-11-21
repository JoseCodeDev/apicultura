from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


# Create your views here.
def iniciar_sesion(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            messages.success(request, f"¡Bienvenido, {user.username}!") 
            next_url = request.POST.get('next', 'productos_mostrar') 
            return redirect(next_url) 
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.") 
    else: 
        form = AuthenticationForm() 
        
    return render(request, 'login/index.html', {'form': form, 'next': request.GET.get('next', '')})


def crerrar_sesion(request): 
    logout(request) 
    messages.success(request, "Has cerrado sesión correctamente.") 
    return redirect('login')