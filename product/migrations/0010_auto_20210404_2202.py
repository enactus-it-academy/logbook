# Generated by Django 3.1.7 on 2021-04-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(verbose_name='Дата покупки товара'),
        ),
    ]
