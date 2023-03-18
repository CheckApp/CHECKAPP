import os
from tkinter import image_names

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image
from utils import utils


class Contato(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    telefone = models.TextField(max_length=11, blank=True, null=True, verbose_name='Telefone')
    mensagem = models.TextField(max_length=100, verbose_name='Mensagem')
    mostrar = models.BooleanField(default=True)
    data_contato = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome



    
