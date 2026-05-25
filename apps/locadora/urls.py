from rest_framework.routers import DefaultRouter

from .views import CarteiraMotoristaViewSet, ClienteViewSet, FuncionarioViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = router.urls
