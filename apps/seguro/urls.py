from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.seguro_list, name='seguro_list'),
    path('criar/', views.seguro_create, name='seguro_create'),
    path('deletar/<int:id>/', views.seguro_delete, name='seguro_delete'),
]
