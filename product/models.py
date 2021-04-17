from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name="Название товара")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    sale_price = models.IntegerField(default=0, verbose_name="Цена на продажу")
    cost_price = models.IntegerField(default=0, verbose_name="Себестоимость")
    count = models.IntegerField(default=0, verbose_name="Количество купленных товаров")
    count_sold = models.IntegerField(default=0, verbose_name="Проданные товары")
    date = models.DateTimeField(verbose_name="Дата покупки товара", auto_now_add=True)
    available_count = models.IntegerField(default=0, verbose_name="Остаток товаров", editable=False)
    earns = models.IntegerField(default=0, verbose_name="Выручка с товара", editable=False)
    total_earns = models.IntegerField(default=0, verbose_name="Выручка", editable=False)

    def save(self, *args, **kwargs):
        self.available_count = self.count - self.count_sold
        self.earns = self.sale_price - self.cost_price
        self.total_earns = self.earns * self.count_sold
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
