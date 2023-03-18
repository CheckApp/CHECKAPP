from django.urls import path

from . import views

app_name = 'suporte'

urlpatterns = [

    path('', views.pageSuporte, name='suporte'),



]
