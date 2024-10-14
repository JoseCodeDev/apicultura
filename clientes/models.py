from django.db import models

# Create your models here.
class Cliente(models.Model):
    OPCIONES_GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=OPCIONES_GENERO)
    telefono = models.CharField(verbose_name="Teléfono", max_length=10)
    email = models.EmailField(max_length=60, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_ultima_compra = models.DateField(verbose_name="Última compra", blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'[nombres={self.nombre}, apellidos={self.apellidos}'