from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name="Название товара")
    sale_price = models.IntegerField(default=0, verbose_name="Цена на продажу")
    cost_price = models.IntegerField(default=0, verbose_name="Себестоимость")
    count = models.IntegerField(default=0, verbose_name="Количество купленных товаров")
    count_sold = models.IntegerField(default=0, verbose_name="Проданные товары")
    date = models.DateTimeField(verbose_name="Дата покупки товара", auto_now_add=True)
    sum = models.IntegerField(default=0, verbose_name="Остаток товаров", editable=False)
    earns_example = models.IntegerField(default=0, verbose_name="Выручка с товара", editable=False)
    earns = models.IntegerField(default=0, verbose_name="Выручка", editable=False)

    def save(self, *args, **kwargs):
        self.sum = self.count - self.count_sold
        self.earns_example = self.sale_price - self.cost_price
        self.earns = self.earns_example * self.count_sold
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


# Product.objects.aggregate(Sum('earns'))
