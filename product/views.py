from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
