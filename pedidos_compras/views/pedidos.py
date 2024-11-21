from django.shortcuts import render, redirect, get_object_or_404
from ..models.pedidos import Pedido
from ..models.detalle_pedidos import DetallePedido
from almacen.models import Insumo
from ..forms.pedidos_form import PedidosForm
from django.contrib import messages
from django.utils import timezone
from django.db import transaction

def mostrar(request): 
    pedidos = Pedido.objects.filter(activo=True) 
    return render(request, 'pedidos/index.html', {'pedidos': pedidos})


def agregar(request): 
    from django.forms import ValidationError
    
    if request.method == 'GET': 
        insumos_activos = Insumo.objects.filter(activo=True)  # Filtrar insumos activos
        return render(request, 'pedidos/agregar.html', {
            'form': PedidosForm(),
            'insumos': insumos_activos
        }) 
    elif request.method == 'POST': 
        form = PedidosForm(request.POST)
        insumos = request.POST.getlist('insumo')  # Lista de insumos
        cantidades = request.POST.getlist('cantidad')  # Lista de cantidades
        precios = request.POST.getlist('precio')  # Lista de precios

        if form.is_valid(): 
            try:
                with transaction.atomic():  # Asegura atomicidad
                    # Guarda el pedido
                    pedido = form.save(commit=False)
                    pedido.empleado = request.user.empleado
                    pedido.total = 0  # Inicializa el total
                    pedido.fecha_pedido = timezone.now() 
                    pedido.save()

                    # Procesa cada insumo del detalle
                    for insumo_id, cantidad, precio in zip(insumos, cantidades, precios):
                        if not insumo_id or not cantidad or not precio:
                            raise ValidationError("Todos los campos del detalle son obligatorios.")
                        
                        detalle = DetallePedido(
                            pedido=pedido,
                            insumo_id=insumo_id,
                            cantidad=int(cantidad),
                            precio=float(precio),
                            activo=True
                        )
                        detalle.save()

                        # Actualiza el total del pedido
                        pedido.total += detalle.cantidad * detalle.precio
                    
                    pedido.save()  # Guarda el total actualizado
                    messages.success(request, 'El pedido y sus detalles se han agregado exitosamente.')
                    return redirect('pedidos_mostrar')
            except ValidationError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, f'Ocurrió un error al procesar el pedido: {e}')
        else: 
            for field, errors in form.errors.items(): 
                for error in errors: 
                    messages.error(request, error)
        
        # Si algo falla, regresa al formulario
        insumos_activos = Insumo.objects.filter(activo=True)
        return render(request, 'pedidos/agregar.html', {
            'form': form,
            'insumos': insumos_activos
        })


def editar(request, id_pedido: int):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
        
    if request.method == 'GET':
        form = PedidosForm(instance=pedido)
        return render(request, 'pedidos/editar.html', {'pedido': pedido, 'form': form})
    elif request.method == 'POST':
        try:
            pedido = get_object_or_404(Pedido, pk=id_pedido)
            form = PedidosForm(request.POST, instance=pedido)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'El pedido se ha editado exitosamente.')
                return redirect('pedidos_mostrar')
            else: 
                for field, errors in form.errors.items(): 
                    for error in errors: 
                        messages.error(request, error) 
                return render(request, 'pedidos/editar.html', {'pedido': pedido, 'form': form}) 
        except ValueError:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'pedidos/editar.html', {'pedido': pedido, 'form': form})


def eliminar(request, id_pedido: int):
    if request.method == 'GET':
        pedido = get_object_or_404(Pedido, pk=id_pedido)
        form = PedidosForm(instance=pedido)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            
        return render(request, 'pedidos/eliminar.html', {'pedido': pedido, 'form': form})
    elif request.method == 'POST':
        try:
            pedido = get_object_or_404(Pedido, pk=id_pedido)
            pedido.activo = False
            pedido.save()
            messages.success(request, 'Pedido eliminado exitosamente.')
                        
            return redirect('pedidos_mostrar')
        except:
            messages.error(request, 'Ocurrió un error, inténtalo de nuevo más tarde.')
            return render(request, 'pedidos/eliminar.html', {'pedido': pedido, 'form': form})
