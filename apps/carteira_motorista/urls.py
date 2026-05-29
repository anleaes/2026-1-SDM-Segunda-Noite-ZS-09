from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.carteira_list, name='carteira_list'),
    path('criar/', views.carteira_create, name='carteira_create'),
    path('deletar/<int:id>/', views.carteira_delete, name='carteira_delete'),
]
