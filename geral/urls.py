from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:id_blog>', views.exibir, name='exibir_pagina'),
]