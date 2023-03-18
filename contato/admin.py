from django.contrib import admin

from . import models
from .models import Contato


class Contato(admin.TabularInline):
    model = models.Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'mensagem')
    list_display_links = ('id', 'nome')

admin.site.register(models.Contato)
