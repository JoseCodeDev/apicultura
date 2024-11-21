from django.shortcuts import render, redirect, get_object_or_404
from ..models.insumos import Insumo
from ..forms.insumos_form import InsumosForm
from django.contrib import messages

def mostrar(request):
    insumos = Insumo.objects.select_related('categoria').filter(activo=True)
    return render(request, 'insumos/index.html', {'insumos': insumos})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'insumos/agregar.html', {'form': InsumosForm})
    elif request.method == 'POST':
        try:
            form = InsumosForm(request.POST)
            if form.is_valid():
                form.stock_actual = 0
                form.save()
                messages.success(request, 'El insumo se ha agregado exitosamente.')
                return redirect('insumos_mostrar')
            else:
                for field, errors in form.errors.items(): 
                    for error in errors: 
                        messages.error(request, error) 
                return render(request, 'insumos/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'insumos/agregar.html', {'form': form})


def editar(request, id_insumo: int):
    insumo = get_object_or_404(Insumo, pk=id_insumo)
        
    if request.method == 'GET':
        form = InsumosForm(instance=insumo)
        return render(request, 'insumos/editar.html', {'insumo': insumo, 'form': form})
    elif request.method == 'POST':
        try:
            insumo = get_object_or_404(Insumo, pk=id_insumo)
            form = InsumosForm(request.POST, instance=insumo)
            
            if form.is_valid(): 
                form.save()
                messages.success(request, 'El insumo se ha editado exitosamente.')
                return redirect('insumos_mostrar')
            else: 
                for field, errors in form.errors.items(): 
                    for error in errors: 
                        messages.error(request, error) 
                return render(request, 'insumos/editar.html', {'insumo': insumo, 'form': form}) 
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'insumos/editar.html', {'insumo': insumo, 'form': form})


def eliminar(request, id_insumo: int):
    
    if request.method == 'GET':
        insumo = get_object_or_404(Insumo, pk=id_insumo)
        form = InsumosForm(instance=insumo)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'insumos/eliminar.html', {'insumo': insumo, 'form': form})
    elif request.method == 'POST':
        try:
            insumo = get_object_or_404(Insumo, pk=id_insumo)
            insumo.activo = False
            insumo.save()
            messages.success(request, 'Insumo eliminado exitosamente.')
                        
            return redirect('insumos_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'insumos/eliminar.html', {'insumo': insumo, 'form': form})
