from rest_framework import serializers
from .models import Product
# from .views import Earns


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class EarnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

