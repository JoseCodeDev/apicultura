from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente
from ..forms.clientes_form import ClientesForm
from django.contrib import messages


def mostrar(request):
    clientes = Cliente.objects.filter(eliminado=False)
    return render(request, 'clientes/index.html', {'clientes': clientes})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'clientes/agregar.html', {'form': ClientesForm})
    elif request.method == 'POST':
        try:
            form = ClientesForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El cliente se ha agregado exitosamente')
                return redirect('clientes_mostrar')
            else:
                if 'genero' in form.errors:
                    messages.error(request, 'Selecciona un género válido')
                    return render(request, 'clients/agregar.html', {'form': form})
                else:
                    messages.error(request, 'Datos no válidos del formulario.')
                    return render(request, 'clientes/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'clientes/agregar.html', {'form': form})


def editar(request, id_cliente: int):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
        
    if request.method == 'GET':
        form = ClientesForm(instance=cliente)
        return render(request, 'clientes/editar.html', {'cliente': cliente, 'form': form})
    elif request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, pk=id_cliente)
            form = ClientesForm(request.POST, instance=cliente)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El cliente se ha editado exitosamente.')
                return redirect('clientes_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'clientes/editar.html', {'cliente': cliente, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'clientes/editar.html', {'cliente': cliente, 'form': form})


def eliminar(request, id_cliente: int):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=id_cliente)
        form = ClientesForm(instance=cliente)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'clientes/eliminar.html', {'cliente': cliente, 'form': form})
    elif request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, pk=id_cliente)
            cliente.eliminado = True
            cliente.save()
            messages.success(request, 'Cliente eliminado exitosamente.')
                        
            return redirect('clientes_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'clientes/eliminar.html', {'cliente': cliente, 'form': form})

