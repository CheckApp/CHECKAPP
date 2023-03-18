# Generated by Django 3.1.2 on 2022-12-19 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('comentarios', '0003_comentario_oficina_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='oficina_comentario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='post_comentario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
            preserve_default=False,
        ),
    ]
