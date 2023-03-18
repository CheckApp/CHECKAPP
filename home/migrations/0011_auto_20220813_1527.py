# Generated by Django 3.1.2 on 2022-08-13 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220812_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newslatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('data_assinatura', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(max_length=250, verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Telefone'),
        ),
    ]