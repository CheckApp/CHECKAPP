# Generated by Django 4.0.1 on 2022-01-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0009_auto_20190815_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='brotinho',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='esfiha',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='especial',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='ingredientes',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='mostrar',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='pizza',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tradicional',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
