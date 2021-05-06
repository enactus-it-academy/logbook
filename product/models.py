from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('account.Owner', on_delete=models.CASCADE, related_name='stores')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, related_name='products')
    sale_price = models.IntegerField("Цена на продажу", default=0)
    cost_price = models.IntegerField("Себестоимость", default=0)
    count = models.IntegerField("Количество купленных товаров", default=0)
    count_sold = models.IntegerField("Проданные товары", default=0)
    date = models.DateTimeField("Дата покупки товара", auto_now_add=True)

    def __str__(self):
        return self.name
