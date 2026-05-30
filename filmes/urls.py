from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes, name='listar_filmes'),
    path('adicionar/', views.adicionar_filme, name='adicionar_filme'),
    path('editar/<int:pk>/', views.editar_filme, name='editar_filme'),
    path('remover/<int:pk>/', views.remover_filme, name='remover_filme'),
]
