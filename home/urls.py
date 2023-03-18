from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homePage.as_view(), name="home"), 
    path('eventos/', views.listaEventos.as_view(), name="eventos"),
    path('projetos/', views.listaProjetos.as_view(), name="projetos"),
    path('sobre/', views.informacoesSobre.as_view(), name="sobre"),
    path('aulas/', views.informacoesAulas.as_view(), name="aulas"),
    path('contato/', views.informacoesContato, name="contato"),
    path('<slug>', views.detalhePost.as_view(), name="detalhe"),
    

    path('como_comprar/', views.informacoesComoComprar.as_view(), name="como_comprar"),
    path('pagamento_e_envio/', views.informacoesPagamentoEnvio.as_view(), name="pagamento_e_envio"),
    path('seguranca/', views.informacoesSeguranca.as_view(), name="seguranca"),
    path('frete/', views.informacoesFrete.as_view(), name="frete"),
    path('trocas_e_devolucoes/', views.informacoesTrocasDevulucoes.as_view(), name="trocas_e_devolucoes"),
    path('garantia/', views.informacoesGarantia.as_view(), name="garantia"),
    path('termos_de_uso/', views.informacoesTermosUso.as_view(), name="termos_de_uso"),
    path('politica_de_privacidade/', views.informacoesPoliticaPrivacidade.as_view(), name="politica_de_privacidade"),
    path('aviso_legal/', views.informacoesAvisoLegal.as_view(), name="aviso_legal"),
    path('documentacao/', views.informacoesDocumentacao.as_view(), name="documentacao"),
]

