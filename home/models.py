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


class Categoria (models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

class Newslatter(models.Model):
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    data_assinatura = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Contato(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    telefone = models.TextField(max_length=50, blank=True, null=True, verbose_name='DDD + Telefone')
    mensagem = models.TextField(max_length=250, verbose_name='Mensagem')
    mostrar = models.BooleanField(default=True)
    data_contato = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class formContato(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='E-mail')
    telefone = models.TextField(max_length=50, blank=True, null=True, verbose_name='Telefone')
    mensagem = models.TextField(max_length=250, verbose_name='Mensagem')
    mostrar = models.BooleanField(default=False)
    data_contato = models.DateTimeField(default=timezone.now)
    usuario_contato = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Post(models.Model):
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')
    eventos = models.BooleanField(default=True, blank=True)
    foto_logo = models.ImageField(
        upload_to='projeto_imagens/%Y/%m/', blank=True, null=True)
    foto_capa = models.ImageField(
        upload_to='projeto_imagens/%Y/%m/', blank=True, null=True)

    titulo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    subtitulo = models.TextField(max_length=50, blank=True, null=True, verbose_name='Sub titulo')
    descricaocurta = models.TextField(max_length=150, blank=True, null=True, verbose_name='Descrição curta')
    descricaolonga = models.TextField(max_length=800, blank=True, null=True, verbose_name='Descrição longa')
    mostrar = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    mapa =models.URLField(max_length=500, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, max_length=50, on_delete=models.DO_NOTHING, blank=True)
    
    
    def __str__(self):
        return self.titulo

    
