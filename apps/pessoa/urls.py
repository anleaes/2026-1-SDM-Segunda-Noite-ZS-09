from django.urls import path

from .views import PessoaInfoView

urlpatterns = [
    path('pessoa/', PessoaInfoView.as_view(), name='pessoa-info'),
]
