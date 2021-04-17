from rest_framework.routers import DefaultRouter

from .views import ProductView

router = DefaultRouter()
router.register(r'products', ProductView)

urlpatterns = router.urls
