from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models
from .models import Categoria, Contato, Newslatter, Post, formContato


class Contato(admin.TabularInline):
    model = models.Contato

class formContato(admin.TabularInline):
    model = models.formContato

class Post(admin.TabularInline):
    model = models.Post

class Newslatter(admin.TabularInline):
    model = models.Newslatter



class formContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'mensagem')
    list_display_links = ('id', 'nome')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'mensagem')
    list_display_links = ('id', 'nome')


class NewslatterAdmin(admin.ModelAdmin):
    list_display = ('email')
    list_display_links = ('email')


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'categoria',)
    list_display_links = ('titulo',)
    list_filter = ('id', 'titulo', 'categoria',)
    list_editable = ('id', 'titulo', 'categoria',)
    list_per_page = 10
    search_fields = ('id', 'titulo', 'categoria',)
    summernote_fields = ('descricaocurta')



admin.site.register(models.Contato)
admin.site.register(models.formContato)
admin.site.register(models.Post)
admin.site.register(models.Categoria)
admin.site.register(models.Newslatter)



