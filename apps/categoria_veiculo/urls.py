from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.categoria_list, name='categoria_list'),
    path('criar/', views.categoria_create, name='categoria_create'),
    path('deletar/<int:id>/', views.categoria_delete, name='categoria_delete'),
]
