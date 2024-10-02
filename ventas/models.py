from django.db import models
from almacen_productos.models import Producto
from django.contrib.auth.models import User
import datetime

# Create your models here.
class MetodosPago(models.Model):
    nombre = models.CharField(max_length=50)


class Venta(models.Model):
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="Usuario")
    fecha_venta = models.DateField(default=datetime.date.today, verbose_name="Fecha de la venta")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Subtotal")
    porcentaje_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Porcentaje de IVA")
    precio_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio del IVA")
    porcentaje_descuento = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Porcentaje de Descuento")
    precio_descuento = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Precio del Descuento")
    metodo_pago = models.ForeignKey(MetodosPago, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Método de pago")
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Total")
    monto_recibido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Monto recibido")
    cambio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Cambio")


class ProductosVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")