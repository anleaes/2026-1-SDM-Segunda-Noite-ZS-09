from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.manutencao_list, name='manutencao_list'),
    path('criar/', views.manutencao_create, name='manutencao_create'),
    path('deletar/<int:id>/', views.manutencao_delete, name='manutencao_delete'),
]
