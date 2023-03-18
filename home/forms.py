from urllib import request

from contato.models import Contato
from django import forms

from . import views


class Contato(forms.Form):
    nome = forms.CharField(max_length=20)

