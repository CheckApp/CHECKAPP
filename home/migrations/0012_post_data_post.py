# Generated by Django 3.1.2 on 2022-09-13 11:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220813_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Publicação'),
        ),
    ]
