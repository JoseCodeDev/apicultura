# Generated by Django 5.0.6 on 2024-11-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_compras', '0004_pedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='observaciones',
            field=models.TextField(blank=True, default='Sin observaciones'),
        ),
    ]
