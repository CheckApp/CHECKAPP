from django.urls import path

from . import views

app_name = 'conteudos'

urlpatterns = [
    path('', views.pageConteudos.as_view(), name="conteudos"), 
    path('especialista/', views.pageTreinamentoEspecialista.as_view(), name="especialista"), 
    path('gerenteRede/', views.pageTreinamentoGerenteRede.as_view(), name="gerenteRede"), 
    path('gerenteLoja/', views.pageTreinamentoGerenteLoja.as_view(), name="gerenteLoja"), 
    path('<slug>', views.pageDetalheFuncionalidades.as_view(), name="detalhe_funcionalidade_especialista"), 
    path('<slug>', views.pageDetalheFuncionalidades.as_view(), name="detalhe_funcionalidade_gerenteRede"), 
    path('<slug>', views.pageDetalheFuncionalidades.as_view(), name="detalhe_funcionalidade_gerenteLoja"), 
]

