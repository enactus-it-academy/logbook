from django.shortcuts import render
from .models import Product
from rest_framework import viewsets, generics, views, status
from django.views.generic import UpdateView
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django.db.models import Sum


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
