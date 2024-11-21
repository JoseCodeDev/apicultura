from django.db import models
from .categorias import Categoria

class Insumo(models.Model):
    sku = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='Sin descripción', verbose_name="Descripción", blank=True, null=True)
    precio_promedio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_minimo = models.IntegerField(verbose_name="Stock mínimo")
    stock_actual = models.IntegerField(verbose_name="Stock actual", default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'insumo'})
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"