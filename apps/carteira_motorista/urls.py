from rest_framework.routers import DefaultRouter

from .views import CarteiraMotoristaViewSet

router = DefaultRouter()
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)

urlpatterns = router.urls
