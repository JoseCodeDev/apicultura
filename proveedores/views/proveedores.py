from django.shortcuts import render, redirect, get_object_or_404
from ..models.proveedores import Proveedor
from ..forms.proveedores_form import ProveedoresForm
from django.contrib import messages

def mostrar(request):
    proveedores = Proveedor.objects.filter(eliminado=False)
    return render(request, 'proveedores/index.html', {'proveedoress': proveedores})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'proveedores/agregar.html', {'form': ProveedoresForm})
    elif request.method == 'POST':
        try:
            form = ProveedoresForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El proveedor se ha agregado exitosamente.')
                return redirect('proveedores_mostrar')
            else:
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'proveedores/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'proveedores/agregar.html', {'form': form})


def editar(request, id_proveedor: int):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
        
    if request.method == 'GET':
        form = ProveedoresForm(instance=proveedor)
        return render(request, 'proveedores/editar.html', {'proveedor': proveedor, 'form': form})
    elif request.method == 'POST':
        try:
            proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
            form = ProveedoresForm(request.POST, instance=proveedor)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El proveedor se ha editado exitosamente.')
                return redirect('proveedores_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'proveedores/editar.html', {'proveedor': proveedor, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'proveedores/editar.html', {'proveedor': proveedor, 'form': form})


def eliminar(request, id_proveedor: int):
    if request.method == 'GET':
        proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
        form = ProveedoresForm(instance=proveedor)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'proveedores/eliminar.html', {'proveedor': proveedor, 'form': form})
    elif request.method == 'POST':
        try:
            proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
            proveedor.activo = False
            proveedor.eliminado = True
            proveedor.save()
            messages.success(request, 'Proveedor eliminado exitosamente.')
                        
            return redirect('proveedores_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'proveedores/eliminar.html', {'proveedor': proveedor, 'form': form})
