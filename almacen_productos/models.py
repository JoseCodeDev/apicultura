from django.db import models
import datetime

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='Sin descripción', verbose_name="Descripción", blank=True)
    stock = models.IntegerField(verbose_name="Stock")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f'[nombre={self.nombre}, stock={self.stock}, categoria={self.categoria.nombre}]'
