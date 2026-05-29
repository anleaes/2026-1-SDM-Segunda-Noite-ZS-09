from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.adicional_list, name='adicional_list'),
    path('criar/', views.adicional_create, name='adicional_create'),
    path('deletar/<int:id>/', views.adicional_delete, name='adicional_delete'),
]
