from django.db import models


class Provedor(models.Model):
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
    direccion_fiscal = models.TextField(verbose_name='Dirección fiscal')
    direccion_envio = models.TextField(verbose_name='Dirección de envío')
    tipo_persona = models.CharField(max_length=6, choices=TIPO_PERSONA, verbose_name='Tipo de persona')
    contacto_nombres = models.CharField(max_length=50, verbose_name='Nombre del contacto')
    contacto_apellidos = models.CharField(max_length=50, verbose_name='Apellidos del contacto')
    contacto_sexo = models.CharField(max_length=9, choices=OPCIONES_SEXO, verbose_name='Sexo del contacto')
    contacto_telefono = models.CharField(max_length=10, verbose_name='Teléfono del contacto')
    contacto_email = models.CharField(max_length=50, verbose_name='Email del contacto')
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Provedor"
        verbose_name_plural = "Provedores"
