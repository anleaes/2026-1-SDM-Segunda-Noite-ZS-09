from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.multa_list, name='multa_list'),
    path('criar/', views.multa_create, name='multa_create'),
    path('deletar/<int:id>/', views.multa_delete, name='multa_delete'),
]
