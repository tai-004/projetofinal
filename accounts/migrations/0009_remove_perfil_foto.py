# Generated by Django 4.0.2 on 2022-07-07 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_perfil_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='foto',
        ),
    ]
