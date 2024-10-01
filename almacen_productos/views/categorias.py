from django.shortcuts import render, redirect, get_object_or_404
from ..models import Categoria
# from ..forms import CategoriasForm
from ..forms.categorias_form import CategoriasForm
from django.contrib import messages


def mostrar(request):
    categorias = Categoria.objects.all()
    
    return render(request, 'categorias/index.html', {'categorias': categorias})


def agregars(request):
    if request.method == 'GET':
        return render(request, 'categorias/agregar.html', {'form': CategoriasForm})
    elif request.method == 'POST':
        try:
            form = CategoriasForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'La categoría se ha agregado exitosamente.')
                return redirect('mostrar_categorias')
            else:
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'categorias/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'categorias/agregar.html', {'form': form, 'error': 'Error al agregar la categoría.'})


def editar(request, id_categoria: int):
    categoria = get_object_or_404(Categoria, pk=id_categoria)
        
    if request.method == 'GET':
        form = CategoriasForm(instance=categoria)
        return render(request, 'categorias/editar.html', {'categoria': categoria, 'form': form})
    elif request.method == 'POST':
        try:
            categoria = get_object_or_404(Categoria, pk=id_categoria)
            form = CategoriasForm(request.POST, instance=categoria)
            if form.is_valid():
                form.save()
                messages.success(request, 'La categoría se ha editado exitosamente.')
                return redirect('mostrar_categorias')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'categorias/editar.html', {'categoria': categoria, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'categorias/editar.html', {'categoria': categoria, 'form': form, 'error': 'Error al editar la categoría.'})


def eliminar(request, id_categoria: int):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, pk=id_categoria)
        form = CategoriasForm(instance=categoria)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'categorias/eliminar.html', {'categoria': categoria, 'form': form})
    elif request.method == 'POST':
        try:
            categoria = get_object_or_404(Categoria, pk=id_categoria)
            categoria.delete()
            messages.success(request, 'Categoría eliminada exitosamente')
                        
            return redirect('mostrar_categorias')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'categorias/eliminar.html', {'categoria': categoria, 'form': form, 'error': 'Error al eliminar la categoria.'})
