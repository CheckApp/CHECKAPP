from urllib import request

from django import forms

from aulas.models import Aulas

from . import views


class Aulas(forms.Form):
    nome = forms.CharField(max_length=20)
