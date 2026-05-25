from rest_framework.routers import DefaultRouter

from .views import ItemAdicionalViewSet

router = DefaultRouter()
router.register(r'itens-adicionais', ItemAdicionalViewSet)

urlpatterns = router.urls
