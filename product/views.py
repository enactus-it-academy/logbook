from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, StoreSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user.owner)

    def perform_create(self, serializer):
        serializer.save()


class StoreAPIView(CreateAPIView, RetrieveAPIView):
    serializer_class = StoreSerializer

    def get_object(self):
        return self.request.user.owner.store

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.owner)
