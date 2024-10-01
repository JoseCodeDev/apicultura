from django.db import models

# Create your models here.
class Estatus(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Categorías de Productos"

    def __str__(self):
        return self.nombre