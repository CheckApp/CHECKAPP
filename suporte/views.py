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
from home.admin import ContatoAdmin
from home.models import FormularioContato
from perfil.models import Perfil
from produto.models import Produto
from suporte import models


def pageSuporte(request):
    if request.method != 'POST':
        form = FormularioContato
        return render(request, 'suporte/suporte.html', {'form': form})

    form = FormularioContato(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário. Verifique os campos e tente novamente!')
        form = FormularioContato(request.POST)
        return render(request, 'suporte/suporte.html', {'form': form})
    
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    mensagem = request.POST.get('mensagem')
    
    if len(nome) < 4:
        messages.error(request, 'Nome invalido! Informe um nome com no mínimo 4 caracteres.')
        form = FormularioContato(request.POST)
        return render(request, 'suporte/suporte.html', {'form': form})
    
    if len(telefone) < 8:
        messages.error(request, 'Telefone inválido! Inclua um telefone válido com DD ou acrescente 9 antes do número do telefone.')
        form = FormularioContato(request.POST)
        return render(request, 'suporte/suporte.html', {'form': form})

    if len(mensagem) < 0:
        messages.error(request, 'Descreva o motivo do contato ')
        form = FormularioContato(request.POST)
        return render(request, 'suporte/suporte.html', {'form': form})

    form.save()
    messages.success(request, 'Mensagem enviada com sucesso!')
    return render(request, 'suporte/suporte.html', {'form': form})