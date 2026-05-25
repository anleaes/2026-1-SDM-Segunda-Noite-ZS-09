from rest_framework.routers import DefaultRouter

from .views import SeguroViewSet

router = DefaultRouter()
router.register(r'seguros', SeguroViewSet)

urlpatterns = router.urls
