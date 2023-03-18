# Generated by Django 3.1.2 on 2022-06-28 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('telefone', models.TextField(blank=True, max_length=50, null=True)),
                ('mensagem', models.TextField(max_length=250)),
                ('mostrar', models.BooleanField(default=True)),
                ('data_contato', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='formContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('telefone', models.TextField(blank=True, max_length=50, null=True)),
                ('mensagem', models.TextField(max_length=250)),
                ('mostrar', models.BooleanField(default=True)),
                ('data_contato', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='home_contato',
        ),
    ]
