# Generated by Django 4.0.5 on 2024-11-17 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar el catálogo'), ('add_vehiculomodel', 'Puede agregar vehículos')]},
        ),
    ]