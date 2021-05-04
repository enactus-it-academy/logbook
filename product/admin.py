from django.contrib import admin
from .models import Product, Store


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'store', 'date']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'date']
