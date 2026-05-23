from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('pessoas/', PessoaViewSet.as_view(), name='pessoa-info'),
]
