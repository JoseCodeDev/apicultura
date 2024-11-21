from django.db import models
from empleados.models import Empleado
from proveedores.models import Proveedor
from django.utils import timezone

class Pedido(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateField(verbose_name='Fecha de pedido')
    estado = models.CharField()
    fecha_entrega = models.DateField(default=timezone.now, verbose_name='Fecha de entrega')
    observaciones = models.TextField(default='Sin observaciones', blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"