from django.db import models
# from models.categorias import Categoria
from .categorias import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='Sin descripción', verbose_name="Descripción", blank=True)
    stock = models.IntegerField(verbose_name="Stock")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'producto'})
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"