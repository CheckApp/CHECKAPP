# Generated by Django 4.0.1 on 2022-08-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_categoria_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='Evento_imagens/%Y/%m/'),
        ),
    ]
