# Generated by Django 5.0.6 on 2024-11-21 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_compras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='departamento',
            new_name='empleado',
        ),
    ]