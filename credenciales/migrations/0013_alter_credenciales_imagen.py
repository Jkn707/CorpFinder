# Generated by Django 5.0.2 on 2024-05-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credenciales', '0012_alter_credenciales_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credenciales',
            name='imagen',
            field=models.ImageField(default='credenciales/images/image_5.png', upload_to='credenciales/images/'),
        ),
    ]