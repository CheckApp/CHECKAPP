# Generated by Django 3.1.2 on 2022-12-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='DDD + Telefone'),
        ),
    ]
