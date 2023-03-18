from django.urls import path

from . import views

app_name = 'contato'

urlpatterns = [
    path('outro/', views.outro.as_view(), name="outro"),
    
]

