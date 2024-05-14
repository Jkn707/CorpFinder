# Generated by Django 5.0.2 on 2024-05-14 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0005_alter_empresa_fecha_extraccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarioscomputrabajo',
            name='autor',
            field=models.CharField(blank=True, default='Anonimo', max_length=255),
        ),
        migrations.AddField(
            model_name='comentarioscomputrabajo',
            name='calificacion',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='comentarioscomputrabajo',
            name='sentimiento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comentarioscomputrabajo',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='webscraping.empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Fecha_extraccion',
            field=models.DateField(default='2024-05-14', null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]