from django.urls import path
from . import views

urlpatterns = [
    path('pessoa/', views.PessoaInfoView.as_view(), name='pessoa-info'),
    path('info/', views.pessoa_info, name='pessoa_info'),
]
