from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('teste', views.teste.as_view(), name='teste'),
    path('oficinas', views.Oficinas.as_view(), name='oficinas'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('estado/<str:estado>', views.PostEstado.as_view(), name='post_estados'),

    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]