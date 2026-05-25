from rest_framework.routers import DefaultRouter

from .views import AgenciaViewSet

router = DefaultRouter()
router.register(r'agencias', AgenciaViewSet)

urlpatterns = router.urls
