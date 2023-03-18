import os
from tkinter import image_names

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image

from aulas.models import Aulas
from contato.models import Contato
from produto.models import Produto
from utils import utils


class FormularioContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar', 'data_contato')
        
class Suporte(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    mensagem = models.TextField(max_length=250, verbose_name='Mensagem')
    
    def __str__(self):
        return self.nome
