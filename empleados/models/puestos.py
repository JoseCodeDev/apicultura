from django.db import models


class Puesto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Sin descripción")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"
    
    def __str__(self):
        return self.nombre