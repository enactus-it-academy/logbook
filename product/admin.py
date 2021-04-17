from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'count_sold', 'sum', 'earns', 'date', 'earns_example']
    list_editable = ['count_sold']
