from dataclasses import fields
from mailbox import NotEmptyError
from msilib.schema import ListView
from re import template
from urllib import request

from contato.views import formulario_contato
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
from home import models
from perfil.models import Perfil

from .models import Aulas


# Create your views here.
class listaAulas(ListView):
    model =  models.Aulas
    template_name = 'aulas/listaAcademias.html'
    context_object_name = 'aulas'
    paginate_by = 10
    ordering = ['-id']
