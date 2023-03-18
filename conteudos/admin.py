from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Funcionalidades


class FuncionalidadesAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_funcionalidade',)
    summernote_fields = ('conteudo_funcionalidade',)
    list_display_links = ('id', 'titulo_funcionalidade')


admin.site.register(Funcionalidades,FuncionalidadesAdmin)
