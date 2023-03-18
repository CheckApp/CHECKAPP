from urllib import request

from django import forms

from contato.models import Suporte

from . import views


class Suporte(forms.Form):
    nome = forms.CharField(max_length=20)

