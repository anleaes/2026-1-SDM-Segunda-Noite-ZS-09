from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.item_list, name='item_list'),
    path('criar/', views.item_create, name='item_create'),
    path('deletar/<int:id>/', views.item_delete, name='item_delete'),
]
