# Generated by Django 3.1.2 on 2022-12-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20221217_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mapa',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]