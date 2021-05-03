from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer, StoreSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.request.user.products.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoreViewSet(ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return self.request.user.stores.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
