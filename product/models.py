from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField("Название товара", max_length=50)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name="Владелец",
                              related_name='products')
    sale_price = models.IntegerField("Цена на продажу", default=0)
    cost_price = models.IntegerField("Себестоимость", default=0)
    count = models.IntegerField("Количество купленных товаров", default=0)
    count_sold = models.IntegerField("Проданные товары", default=0)
    date = models.DateTimeField("Дата покупки товара", auto_now_add=True)
    available_count = models.IntegerField("Остаток товаров", default=0, editable=False)
    earns = models.IntegerField("Выручка с товара", default=0, editable=False)
    total_earns = models.IntegerField("Выручка", default=0, editable=False)

    def save(self, *args, **kwargs):
        self.available_count = self.count - self.count_sold
        self.earns = self.sale_price - self.cost_price
        self.total_earns = self.earns * self.count_sold
        super(Product, self).save(*args, **kwargs)
