from django.contrib import admin

from . import models
from .models import Suporte


class SuporteAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'mensagem']


admin.site.register(models.Suporte)
