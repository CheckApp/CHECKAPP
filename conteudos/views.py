from dataclasses import fields
from mailbox import NotEmptyError
from re import template
from urllib import request

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

import suporte
from contato.views import formulario_contato
from conteudos.admin import FuncionalidadesAdmin
from conteudos.models import Funcionalidades
from home.admin import ContatoAdmin
from home.models import FormularioContato
from perfil.models import Perfil
from produto.models import Produto
from suporte import models


# Create your views here.
class pageConteudos(ListView):
    model = models.Aulas
    template_name = 'conteudos/conteudos.html'

class pageTreinamentoEspecialista(ListView):
    model = Funcionalidades
    template_name = 'conteudos/especialista.html'
    context_object_name = 'funcionalidade'
    paginate_by = 6
    ordering = ['-id']

class pageDetalheFuncionalidades(DetailView):
    model = Funcionalidades
    template_name = 'conteudos/detalhe_funcionalidade_especialista.html'
    template_name = 'conteudos/detalhe_funcionalidade_gerenteLoja.html'
    template_name = 'conteudos/detalhe_funcionalidade_gerenteRede.html'
    context_object_name = 'funcionalidade'
    slug_url_kwarg = 'slug'
    

class pageTreinamentoGerenteRede(ListView):
    model = Funcionalidades
    context_object_name = 'funcionalidade'
    paginate_by = 6
    ordering = ['-id']
    template_name = 'conteudos/gerenteRede.html'

class pageTreinamentoGerenteLoja(ListView):
    model = models.Aulas
    model = Funcionalidades
    context_object_name = 'funcionalidade'
    paginate_by = 6
    ordering = ['-id']
    template_name = 'conteudos/gerenteLoja.html'
