from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, StoreAPIView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('store/', StoreAPIView.as_view()),
]

urlpatterns += router.urls
