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


class Funcionalidades(models.Model):
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    exibir_funcionalidade = models.BooleanField(default=True, verbose_name='Exibir esta funcionalidade?')
    funcionalidade_especialista = models.BooleanField(default=False, verbose_name='Funcionalidade de Especialista?')
    funcionalidade_GerenteLoja = models.BooleanField(default=False, verbose_name='Funcionalidade de Gerente de Loja?')
    funcionalidade_GerenteRede = models.BooleanField(default=False, verbose_name='funcionalidade de Gerente de rede?')
    titulo_funcionalidade = models.CharField(max_length=255, verbose_name='Título da funiocnalidade')
    subtitulo_funcionalidade = models.CharField(max_length=255, verbose_name='Sub-título da funcionalidade')
    autor_publicacao = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor da publicação')
    conteudo_funcionalidade = models.TextField(verbose_name='Conteúdo')
    icone_funcionalidade = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True,
                                    null=True, verbose_name='Imagem do icone da funcionalidade')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug do final do link')
    
    def __str__(self):
        return self.titulo_funcionalidade

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.icone_funcionalidade:
            self.resize_image(self.icone_funcionalidade.name, 800)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close()