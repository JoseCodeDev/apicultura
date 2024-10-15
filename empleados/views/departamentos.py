from django.shortcuts import render, redirect, get_object_or_404
from ..models.departamentos import Departamento
from ..forms.departamentos_form import DepartamentosForm
from django.contrib import messages

def mostrar(request):
    departamentos = Departamento.objects.filter(activo=True)
    return render(request, 'departamentos/index.html', {'departamentos': departamentos})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'departamentos/agregar.html', {'form': DepartamentosForm})
    elif request.method == 'POST':
        try:
            form = DepartamentosForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El departamento se ha agregado exitosamente.')
                return redirect('departamentos_mostrar')
            else:
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'departamento/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'departamentos/agregar.html', {'form': form})


def editar(request, id_departamento: int):
    departamento = get_object_or_404(Departamento, pk=id_departamento)
        
    if request.method == 'GET':
        form = DepartamentosForm(instance=departamento)
        return render(request, 'departamentos/editar.html', {'departamento': departamento, 'form': form})
    elif request.method == 'POST':
        try:
            departamento = get_object_or_404(Departamento, pk=id_departamento)
            form = DepartamentosForm(request.POST, instance=departamento)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El departamento se ha editado exitosamente.')
                return redirect('departamentos_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'departamentos/editar.html', {'departamento': departamento, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'departamentos/editar.html', {'departamento': departamento, 'form': form})


def eliminar(request, id_departamento: int):
    if request.method == 'GET':
        departamento = get_object_or_404(Departamento, pk=id_departamento)
        form = DepartamentosForm(instance=departamento)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'departamentos/eliminar.html', {'departamento': departamento, 'form': form})
    elif request.method == 'POST':
        try:
            departamento = get_object_or_404(Departamento, pk=id_departamento)
            departamento.activo = False
            departamento.save()
            messages.success(request, 'Departamento eliminado exitosamente.')
                        
            return redirect('departamentos_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'departamentos/eliminar.html', {'departamento': departamento, 'form': form})
