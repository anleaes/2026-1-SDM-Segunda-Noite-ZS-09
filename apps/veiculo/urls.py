from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.veiculo_list, name='veiculo_list'),
    path('criar/', views.veiculo_create, name='veiculo_create'),
    path('deletar/<int:id>/', views.veiculo_delete, name='veiculo_delete'),
]
