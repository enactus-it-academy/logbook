from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, StoreSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user.owner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoreViewSet(ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return self.request.user.stores.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
