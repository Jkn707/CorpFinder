# Generated by Django 5.0.2 on 2024-05-16 07:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0008_alter_empresa_fecha_extraccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarioscomputrabajo',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='comentariospropios',
            name='calificacion',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
