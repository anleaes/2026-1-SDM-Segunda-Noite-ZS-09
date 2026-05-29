from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.reserva_list, name='reserva_list'),
    path('criar/', views.reserva_create, name='reserva_create'),
    path('deletar/<int:id>/', views.reserva_delete, name='reserva_delete'),
]
