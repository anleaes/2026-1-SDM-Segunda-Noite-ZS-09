from rest_framework.routers import DefaultRouter

from .views import CarteiraMotoristaViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)

urlpatterns = router.urls
