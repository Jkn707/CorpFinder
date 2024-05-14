# Generated by Django 5.0.2 on 2024-05-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0011_alter_empresa_id'),
        ('credenciales', '0007_alter_credenciales_empresas_favoritas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credenciales',
            old_name='archivo_pdf',
            new_name='CV',
        ),
        migrations.AlterField(
            model_name='credenciales',
            name='empresas_favoritas',
            field=models.ManyToManyField(to='corp.empresa'),
        ),
    ]