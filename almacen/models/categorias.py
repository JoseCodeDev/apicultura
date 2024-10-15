from django.db import models

class Categoria(models.Model):
    TIPO_CATEGORIA = [
        ('producto', 'Producto'),
        ('insumo', 'Insumo'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CATEGORIA)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f"{self.nombre}"