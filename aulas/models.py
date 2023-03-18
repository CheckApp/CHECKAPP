import os
from tkinter import image_names

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image
from utils import utils


class Aulas(models.Model):
    academia = models.CharField(max_length=50, blank=True, null=True, verbose_name='Academia')
    mestre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Mestre')
    contraMestre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Contra Mestre')
    professor = models.CharField(max_length=50, blank=True, null=True, verbose_name='Professor')
    dias = models.CharField(max_length=50, blank=True, null=True, verbose_name='Dias')
    horario_de = models.CharField(max_length=50, blank=True, null=True, verbose_name='Horário de')
    horario_ate = models.CharField(max_length=50, blank=True, null=True, verbose_name='Horário ate')
    endereco = models.CharField(max_length=150, blank=True, null=True, verbose_name='Endereço')
    pagamento = models.CharField(max_length=50, blank=True, null=True, verbose_name='Pagamento')
    modalidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Modalidade')
    mostrar = models.BooleanField(default=True, verbose_name='Publicar')
    online = models.BooleanField(default=True, verbose_name='Aula online')
    presencial = models.BooleanField(default=True, verbose_name='Aula presencial' )

    def __str__(self):
        return self.academia
