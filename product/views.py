<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
=======
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer, SellSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductCreateView(CreateAPIView, LoginRequiredMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> auth


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class SellView(UpdateAPIView):
    serializer_class = SellSerializer
    queryset = Product.objects.all()


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

