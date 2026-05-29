from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.cliente_list, name='cliente_list'),
    path('criar/', views.cliente_create, name='cliente_create'),
    path('deletar/<int:id>/', views.cliente_delete, name='cliente_delete'),
]
