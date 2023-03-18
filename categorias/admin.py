from django.contrib import admin

from .models import (Assinatura, Bairro, Bandeira, Categoria, Cidade,
                     Consultor, Estado, Perfil, Rede, SistemaPDV, Uso)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_links = ('id', 'nome_cat')
class AssinaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'assinatura')
    list_display_links = ('id', 'assinatura')
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')
    list_display_links = ('id', 'estado')
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cidade')
    list_display_links = ('id', 'cidade')
class BairroAdmin(admin.ModelAdmin):
    list_display = ('id', 'bairro')
    list_display_links = ('id', 'bairro')
class SistemaPDVAdmin(admin.ModelAdmin):
    list_display = ('id', 'sistemaPDV')
    list_display_links = ('id', 'sistemaPDV')
class ConsultorAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultor')
    list_display_links = ('id', 'consultor')
class BandeiraAdmin(admin.ModelAdmin):
    list_display = ('id', 'bandeira')
    list_display_links = ('id', 'bandeira')
class RedeAdmin(admin.ModelAdmin):
    list_display = ('id', 'rede')
    list_display_links = ('id', 'rede')
class UsoAdmin(admin.ModelAdmin):
    list_display = ('id', 'uso')
    list_display_links = ('id', 'uso')
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil')
    list_display_links = ('id', 'perfil')




admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(SistemaPDV, SistemaPDVAdmin)
admin.site.register(Consultor, ConsultorAdmin)
admin.site.register(Bandeira, BandeiraAdmin)
admin.site.register(Rede, RedeAdmin)
admin.site.register(Uso, UsoAdmin)
admin.site.register(Perfil, PerfilAdmin)

