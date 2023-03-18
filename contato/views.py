from dataclasses import fields
from mailbox import NotEmptyError
from re import template
from urllib import request

from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from home.admin import ContatoAdmin
from perfil.models import Perfil

from contato.forms import Contato, formContato

from . import models


class outro(View):
    template_name = 'contato/outro.html'

def formulario_contato(request):
    return render(request, "contato/contato.html")
    if request.method == "GET":
        form = formContato()
        context = {
            'form' : form
        }
        return render(request, "contato/contato.html", context=context)
    else:
        form = formContato(request.POST)
        if form.is_valid():
            contato = form.save()
            form = formContato()
            messages.success(request, 'Mensagem enviada!')
        
        context={
            'form': form
        }  
        return render(request, "contato/contato.html", context=context)
