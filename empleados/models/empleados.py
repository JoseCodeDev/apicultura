from django.db import models
from .puestos import Puesto
from .departamentos import Departamento


class Empleado(models.Model):
    OPCIONES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    OPCIONES_PARENTESCO = [
        ('Madre', 'Madre'),
        ('Padre', 'Padre'),
        ('Hermanos', 'Hermano(a)'),
        ('Esposos', 'Esposo(a)'),
        ('Novios', 'Novio(a)'),
        ('Otro', 'Otro'),
    ]
    
    GRUPOS_SANGUINEOS = [
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=OPCIONES_SEXO)
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    grupo_sanguineo = models.CharField(max_length=3, choices=GRUPOS_SANGUINEOS, verbose_name='Grupo sanguíneo')
    fecha_contratacion = models.DateField(verbose_name='Fecha de contratación')
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fecha_alta_ss = models.DateField(verbose_name='Fecha de alta en SS')
    nss = models.CharField(max_length=11, verbose_name='NSS')
    clabe_interbancaria = models.CharField(max_length=18, verbose_name='CLABE interbancaria')
    contacto_emergencia_nombres = models.CharField(max_length=50, verbose_name='Nombres de contacto de emergencia')
    contacto_emergencia_apellidos = models.CharField(max_length=50, verbose_name='Apellidos de contacto de emergencia')
    contacto_emergencia_telefono = models.CharField(max_length=10, verbose_name='Teléfono de contacto de emergencia')
    contacto_emergencia_parentesco = models.CharField(max_length=10, choices=OPCIONES_PARENTESCO, verbose_name='Parentesco de contacto de emergencia')
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
