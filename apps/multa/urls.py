from rest_framework.routers import DefaultRouter

from .views import MultaViewSet

router = DefaultRouter()
router.register(r'multas', MultaViewSet)

urlpatterns = router.urls
