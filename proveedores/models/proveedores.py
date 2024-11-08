from django.db import models


class Proveedor(models.Model):
    OPCIONES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    TIPO_PERSONA = [
        ('Moral', 'Moral'),
        ('Fisica', 'Física'),
    ]

    nombre_empresa = models.CharField(max_length=100, verbose_name='Nombre de la empresa')
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    direccion = models.TextField(verbose_name='Dirección')
    telefono_empresa = models.CharField(max_length=12, verbose_name='Teléfono de la empresa')
    email_empresa = models.CharField(max_length=50, verbose_name='Email de la empresa')
    tipo_persona = models.CharField(max_length=6, choices=TIPO_PERSONA, verbose_name='Tipo de persona')
    banco = models.CharField(max_length=100, verbose_name='Nombre del banco')
    numero_cuenta = models.CharField(max_length=18, verbose_name='Número de cuenta')
    representante_nombres = models.CharField(max_length=50, verbose_name='Nombre del representante')
    representante_apellidos = models.CharField(max_length=50, verbose_name='Apellidos del representante')
    representante_sexo = models.CharField(max_length=9, choices=OPCIONES_SEXO, verbose_name='Sexo del representante')
    representante_telefono = models.CharField(max_length=10, verbose_name='Teléfono del representante')
    representante_email = models.CharField(max_length=50, verbose_name='Email del representante')
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
