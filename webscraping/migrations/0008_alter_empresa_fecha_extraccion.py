# Generated by Django 5.0.1 on 2024-05-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0007_alter_comentarioscomputrabajo_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Fecha_extraccion',
            field=models.DateField(default='2024-05-16', null=True),
        ),
    ]