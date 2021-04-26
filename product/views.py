from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.request.user.products.all()
