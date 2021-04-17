from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'available_count', 'count_sold', 'earns', 'date', 'total_earns']
    list_editable = ['count_sold']
