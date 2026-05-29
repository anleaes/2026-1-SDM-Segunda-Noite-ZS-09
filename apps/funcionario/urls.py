from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.funcionario_list, name='funcionario_list'),
    path('criar/', views.funcionario_create, name='funcionario_create'),
    path('deletar/<int:id>/', views.funcionario_delete, name='funcionario_delete'),
]
