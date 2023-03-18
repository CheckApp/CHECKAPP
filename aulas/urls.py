from django.urls import path

from . import views

app_name = 'aulas'

urlpatterns = [
    path('', views.listaAulas.as_view(), name="listaAcademias"), 

]

