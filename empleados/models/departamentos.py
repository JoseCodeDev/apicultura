from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Sin descripción")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"