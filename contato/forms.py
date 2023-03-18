from urllib import request

from django import forms

from .models import Contato


class formContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome', 'email')
