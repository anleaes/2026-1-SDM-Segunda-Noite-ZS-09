from rest_framework.routers import DefaultRouter

from .views import CategoriaVeiculoViewSet

router = DefaultRouter()
router.register(r'categorias-veiculo', CategoriaVeiculoViewSet)

urlpatterns = router.urls
