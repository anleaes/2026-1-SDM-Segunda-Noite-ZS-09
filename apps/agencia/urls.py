from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.agencia_list, name='agencia_list'),
    path('criar/', views.agencia_create, name='agencia_create'),
    path('deletar/<int:id>/', views.agencia_delete, name='agencia_delete'),
]
