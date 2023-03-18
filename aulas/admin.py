from django.contrib import admin

from . import models
from .models import Aulas


class Aulas(admin.TabularInline):
    model = models.Aulas



class AulasAdmin(admin.ModelAdmin):
    list_display = ('id','academia', 'mestre', 'contramestre', 'professor')
    list_display_links = ('id','academia', 'mestre', 'contramestre', 'professor')




admin.site.register(models.Aulas)
