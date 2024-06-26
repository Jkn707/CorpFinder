# Generated by Django 5.0.2 on 2024-05-16 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0006_comentarioscomputrabajo_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarioscomputrabajo',
            name='autor',
            field=models.CharField(blank=True, default='Anónimo', max_length=255),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Fecha_extraccion',
            field=models.DateField(default='2024-05-15', null=True),
        ),
        migrations.CreateModel(
            name='ComentariosPropios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(blank=True, max_length=255, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('calificacion', models.IntegerField(blank=True, default=0, null=True)),
                ('sentimiento', models.CharField(blank=True, max_length=255, null=True)),
                ('autor', models.CharField(blank=True, default='Anónimo', max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_propios', to='webscraping.empresa')),
            ],
        ),
    ]
