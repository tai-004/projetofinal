# Generated by Django 4.0.2 on 2022-06-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0003_estagio_criado_por'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estagio',
            options={'permissions': (('est', 'est'), ('criar', 'criar'), ('exc', 'exc'))},
        ),
    ]