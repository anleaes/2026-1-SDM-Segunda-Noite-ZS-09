from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.pagamento_list, name='pagamento_list'),
    path('criar/', views.pagamento_create, name='pagamento_create'),
    path('deletar/<int:id>/', views.pagamento_delete, name='pagamento_delete'),
]
