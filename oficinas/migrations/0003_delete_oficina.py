# Generated by Django 3.1.2 on 2022-12-19 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_auto_20221219_1140'),
        ('oficinas', '0002_auto_20221218_1954'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Oficina',
        ),
    ]
