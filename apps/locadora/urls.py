from rest_framework.routers import DefaultRouter

from .views import AgenciaViewSet, CarteiraMotoristaViewSet, ClienteViewSet, FuncionarioViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'agencias', AgenciaViewSet)

urlpatterns = router.urls
