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

from contato.views import formulario_contato
from home.admin import ContatoAdmin
from perfil.models import Perfil
from produto.models import Produto

from . import models
from .models import Contato, FormularioContato, Newslatter

# ---- TESTE DE PAGINA -----

#class listaProdutosPizzas(View):
#    def get(self, *args, **kwargs):
#       return HttpResponse('oi')





class homePage(ListView):
    model =  models.Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-id']
    
    

    

    




# ---- LISTAGEM DE EVENTOS E PROJETOS SOCIAIS -----

class listaEventos(ListView):
    model =  models.Post
    template_name = 'home/eventos.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-id']


class listaProjetos(ListView):
    model =  models.Post
    template_name = 'home/projetos.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-id']



# ---- EXIBIÇÃO DO DETALHE DO POST (projetos sociais e eventos) -----

class detalhePost(DetailView):
    model = models.Post
    template_name = 'home/detalhe.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


# ---- páginas -----

class informacoesSobre(ListView):
    model = models.Post
    template_name = 'home/sobre.html'

class informacoesAulas(ListView):
    model = models.Aulas
    template_name = 'home/aulas.html'
    context_object_name = 'aulas'
    paginate_by = 6
    ordering = ['-id']


def informacoesContato(request):
    if request.method != 'POST':
        form = FormularioContato
        return render(request, 'home/contato.html', {'form': form})

    form = FormularioContato(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário. Verifique os campos e tente novamente!')
        form = FormularioContato(request.POST)
        return render(request, 'home/contato.html', {'form': form})
    
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    mensagem = request.POST.get('mensagem')
    
    if len(nome) < 4:
        messages.error(request, 'Nome invalido! Informe um nome com no mínimo 4 caracteres.')
        form = FormularioContato(request.POST)
        return render(request, 'home/contato.html', {'form': form})
    
    if len(telefone) < 8:
        messages.error(request, 'Telefone inválido! Inclua um telefone válido com DD ou acrescente 9 antes do número do telefone.')
        form = FormularioContato(request.POST)
        return render(request, 'home/contato.html', {'form': form})

    if len(mensagem) < 0:
        messages.error(request, 'Descreva o motivo do contato ')
        form = FormularioContato(request.POST)
        return render(request, 'home/contato.html', {'form': form})

    form.save()
    messages.success(request, 'Mensagem enviada com sucesso!')
    return render(request, 'home/contato.html', {'form': form})
    
class informacoesComoComprar(ListView):
    model = models.Post
    template_name = 'home/como_comprar.html'

class informacoesPagamentoEnvio(ListView):
    model = models.Post
    template_name = 'home/pagamento_e_envio.html'

class informacoesSeguranca(ListView):
    model = models.Post
    template_name = 'home/seguranca.html'

class informacoesFrete(ListView):
    model = models.Post
    template_name = 'home/frete.html'

class informacoesTrocasDevulucoes(ListView):
    model = models.Post
    template_name = 'home/trocas_e_devolucoes.html'

class informacoesGarantia(ListView):
    model = models.Post
    template_name = 'home/garantia.html'

class informacoesTermosUso(ListView):
    model = models.Post
    template_name = 'home/termos_de_uso.html'
    
class informacoesPoliticaPrivacidade(ListView):
    model = models.Post
    template_name = 'home/politica_de_privacidade.html'

class informacoesAvisoLegal(ListView):
    model = models.Post
    template_name = 'home/aviso_legal.html'

class informacoesDocumentacao(ListView):
    model = models.Post
    template_name = 'home/documentacao.html'

