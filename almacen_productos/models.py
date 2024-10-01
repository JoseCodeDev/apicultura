from django.db import models
import datetime

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Sin descripción", null=True, blank=True, verbose_name="Descripción")
    stock = models.IntegerField(verbose_name="Stock")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Venta")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    fecha_agregado = models.DateField(default=datetime.date.today, verbose_name="Fecha de Agregado")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f'[nombre={self.nombre}, stock={self.stock}, categoria={self.categoria.nombre}]'
