# Generated by Django 5.0.6 on 2024-10-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen_productos', '0008_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
