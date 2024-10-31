from django.shortcuts import render, redirect, get_object_or_404
from ..models.empleados import Empleado
from ..forms.empleados_form import EmpleadosForm
from django.contrib import messages

def mostrar(request):
    empleados = Empleado.objects.filter(eliminado=False)
    return render(request, 'empleados/index.html', {'empleados': empleados})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'empleados/agregar.html', {'form': EmpleadosForm})
    elif request.method == 'POST':
        try:
            form = EmpleadosForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El empleado se ha agregado exitosamente.')
                return redirect('empleados_mostrar')
            else:
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'empleado/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'empleados/agregar.html', {'form': form})


def editar(request, id_empleado: int):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
        
    if request.method == 'GET':
        form = EmpleadosForm(instance=empleado)
        return render(request, 'empleados/editar.html', {'empleado': empleado, 'form': form})
    elif request.method == 'POST':
        try:
            empleado = get_object_or_404(Empleado, pk=id_empleado)
            form = EmpleadosForm(request.POST, instance=empleado)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El empleado se ha editado exitosamente.')
                return redirect('empleados_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'empleados/editar.html', {'empleado': empleado, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'empleados/editar.html', {'empleado': empleado, 'form': form})


def eliminar(request, id_empleado: int):
    if request.method == 'GET':
        empleado = get_object_or_404(Empleado, pk=id_empleado)
        form = EmpleadosForm(instance=empleado)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'empleados/eliminar.html', {'empleado': empleado, 'form': form})
    elif request.method == 'POST':
        try:
            empleado = get_object_or_404(Empleado, pk=id_empleado)
            empleado.activo = False
            empleado.save()
            messages.success(request, 'empleado eliminado exitosamente.')
                        
            return redirect('empleados_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'empleados/eliminar.html', {'empleado': empleado, 'form': form})
