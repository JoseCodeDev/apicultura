# Generated by Django 5.0.6 on 2024-10-14 22:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('producto', 'Producto'), ('insumo', 'Insumo')], max_length=10)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, default='Sin descripción', null=True, verbose_name='Descripción')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(limit_choices_to={'tipo': 'insumo'}, on_delete=django.db.models.deletion.CASCADE, to='almacen.categoria')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, default='Sin descripción', verbose_name='Descripción')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de venta')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('categoria', models.ForeignKey(limit_choices_to={'tipo': 'producto'}, on_delete=django.db.models.deletion.CASCADE, to='almacen.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
