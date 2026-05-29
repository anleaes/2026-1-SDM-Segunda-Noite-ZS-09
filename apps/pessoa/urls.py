from django.urls import path
from . import views

urlpatterns = [
    path('pessoa/', views.PessoaInfoView.as_view(), name='pessoa-info'),
]
