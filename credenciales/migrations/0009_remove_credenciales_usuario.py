# Generated by Django 5.0.2 on 2024-05-14 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credenciales', '0008_rename_archivo_pdf_credenciales_cv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credenciales',
            name='usuario',
        ),
    ]
