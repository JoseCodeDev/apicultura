from django.db import models
# from models.categorias import Categoria
from .categorias import Categoria
from datetime import date

class Producto(models.Model):
    sku = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='Sin descripción', verbose_name="Descripción", blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'producto'})
    stock_minimo = models.IntegerField(verbose_name="Stock mínimo")
    stock_actual = models.IntegerField(verbose_name="Stock actual", default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=16)
    ganancia = models.DecimalField(max_digits=10, decimal_places=2)
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    fecha_ingreso = models.DateField(default=date.today)
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"