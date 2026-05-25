from rest_framework.routers import DefaultRouter

from .views import (
    AgenciaViewSet,
    CarteiraMotoristaViewSet,
    CategoriaVeiculoViewSet,
    ClienteViewSet,
    FuncionarioViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'agencias', AgenciaViewSet)
router.register(r'categorias-veiculo', CategoriaVeiculoViewSet)
router.register(r'veiculos', VeiculoViewSet)

urlpatterns = router.urls
