# Generated by Django 5.0.2 on 2024-05-14 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credenciales', '0009_remove_credenciales_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='credenciales',
            name='usuario',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='credenciales', to=settings.AUTH_USER_MODEL),
        ),
    ]
