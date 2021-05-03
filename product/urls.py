from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, StoreViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = router.urls
