from django.db import models
from almacen.models import Insumo
from ..models.pedidos import Pedido

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Detalle del pedido"
        verbose_name_plural = "Detalle de los pedidos"