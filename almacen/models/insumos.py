from django.db import models
from .categorias import Categoria

class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='Sin descripción', verbose_name="Descripción", blank=True, null=True)
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, limit_choices_to={'tipo': 'insumo'})
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"