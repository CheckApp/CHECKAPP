import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

from categorias.models import (Assinatura, Bairro, Bandeira, Categoria, Cidade,
                               Consultor, Estado, Perfil, Rede, SistemaPDV,
                               Uso)


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    data_fim = models.DateTimeField(default=timezone.now,  verbose_name='Data de encerramento')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    
    

    pagando = models.BooleanField(default=True, verbose_name='O cliente esta pagando?')
    valor_mensalidade = models.CharField(max_length=10, verbose_name='Valor da mensalidade')
    tipo_assinatura = models.ForeignKey(Assinatura, on_delete=models.DO_NOTHING,
                                    blank=True, null=True, verbose_name='Tipo de assinatura')
    cnpj = models.CharField(max_length=15, verbose_name='CNPJ')
    inscricao_estadual = models.CharField(max_length=10, verbose_name='Inscricao estadual')
    email_oficina = models.EmailField(max_length=50, null=True, verbose_name='Email da loja')
    contato_oficina = models.TextField(max_length=50, blank=True, null=True, verbose_name='DDD + Telefone da oficina')

    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING,
                                        blank=True, null=True, verbose_name='Estado')
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING,
                                        blank=True, null=True, verbose_name='Cidade')
    bairro = models.ForeignKey(Bairro, on_delete=models.DO_NOTHING,
                                        blank=True, null=True, verbose_name='Bairro')
    numero_residencia = models.CharField(max_length=8,  verbose_name='Numero da residência')
    cep = models.CharField(max_length=8, verbose_name='CEP do endereço')
    complemento = models.CharField(max_length=100, verbose_name='Complemento endereço')

    sistema_pdv = models.ForeignKey(SistemaPDV, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Sistema do PDV')

    integrado = models.BooleanField(default=True, blank=True, verbose_name='Esta Integrado?')
    contato_pdv = models.CharField(max_length=255, blank=True, verbose_name='Contato do sistema PDV')
    anydesk = models.TextField(max_length=10, blank=True, verbose_name='Acesso Anydesk')
    teamviewer = models.TextField(max_length=10, blank=True, verbose_name='Acesso TeamViewer')

    consultor = models.ForeignKey(Consultor, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Consultor ou revendedor')

    bandeira = models.ForeignKey(Bandeira, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Bandeira do posto')
    
    rede_grupo = models.ForeignKey(Rede, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Rede ou grupo')
    
    uso_momento = models.ForeignKey(Uso, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Modo de uso atual')
    
    perfil_cliente = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Perfil do cliente')

    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,
                                       blank=True, null=True, verbose_name='Categoria')

    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True,
                                    null=True, verbose_name='Foto do posto')

    publicado_post = models.BooleanField(default=False, verbose_name='Publicar no site')

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem_post:
            self.resize_image(self.imagem_post.name, 800)

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
