from django.shortcuts import render, redirect, get_object_or_404
from ..models import Producto
# from ..forms import ProductosForm
from ..forms.productos_form import ProductosForm
from django.contrib import messages

def mostrar(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'productos/index.html', {'productos': productos})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'productos/agregar.html', {'form': ProductosForm})
    elif request.method == 'POST':
        try:
            form = ProductosForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El producto se ha agregado exitosamente.')
                return redirect('productos_mostrar')
            else:
                if 'categoria' in form.errors:
                    messages.error(request, 'Selecciona una categoría válida.')
                    return render(request, 'productos/agregar.html', {'form': form})
                else:
                    messages.error(request, 'Datos no válidos del formulario.')
                    return render(request, 'productos/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'productos/agregar.html', {'form': form})


def editar(request, id_producto: int):
    producto = get_object_or_404(Producto, pk=id_producto)
        
    if request.method == 'GET':
        form = ProductosForm(instance=producto)
        return render(request, 'productos/editar.html', {'producto': producto, 'form': form})
    elif request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, pk=id_producto)
            form = ProductosForm(request.POST, instance=producto)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El producto se ha editado exitosamente.')
                return redirect('productos_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'productos/editar.html', {'producto': producto, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'productos/editar.html', {'producto': producto, 'form': form})


def eliminar(request, id_producto: int):
    
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=id_producto)
        form = ProductosForm(instance=producto)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'productos/eliminar.html', {'producto': producto, 'form': form})
    elif request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, pk=id_producto)
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente.')
                        
            return redirect('productos_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'productos/eliminar.html', {'producto': producto, 'form': form})
