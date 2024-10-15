from django.shortcuts import render, redirect, get_object_or_404
from ..models.puestos import Puesto
from ..forms.puestos_form import PuestosForm
from django.contrib import messages

def mostrar(request):
    puestos = Puesto.objects.filter(activo=True)
    return render(request, 'puestos/index.html', {'puestos': puestos})


def agregar(request):
    if request.method == 'GET':
        return render(request, 'puestos/agregar.html', {'form': PuestosForm})
    elif request.method == 'POST':
        try:
            form = PuestosForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El puesto se ha agregado exitosamente.')
                return redirect('puestos_mostrar')
            else:
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'puestos/agregar.html', {'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'puestos/agregar.html', {'form': form})


def editar(request, id_puesto: int):
    puesto = get_object_or_404(Puesto, pk=id_puesto)
        
    if request.method == 'GET':
        form = PuestosForm(instance=puesto)
        return render(request, 'puestos/editar.html', {'puesto': puesto, 'form': form})
    elif request.method == 'POST':
        try:
            puesto = get_object_or_404(Puesto, pk=id_puesto)
            form = PuestosForm(request.POST, instance=puesto)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El puesto se ha editado exitosamente.')
                return redirect('puestos_mostrar')
            else: 
                messages.error(request, 'Datos no válidos del formulario.')
                return render(request, 'puestos/editar.html', {'puesto': puesto, 'form': form})
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'puestos/editar.html', {'puesto': puesto, 'form': form})


def eliminar(request, id_puesto: int):
    
    if request.method == 'GET':
        puesto = get_object_or_404(Puesto, pk=id_puesto)
        form = PuestosForm(instance=puesto)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'puestos/eliminar.html', {'puesto': puesto, 'form': form})
    elif request.method == 'POST':
        try:
            puesto = get_object_or_404(Puesto, pk=id_puesto)
            puesto.activo = False
            puesto.save()
            messages.success(request, 'Puesto eliminado exitosamente.')
                        
            return redirect('puestos_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'puestos/eliminar.html', {'puesto': puesto, 'form': form})
