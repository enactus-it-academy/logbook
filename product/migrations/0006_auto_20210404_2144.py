# Generated by Django 3.1.7 on 2021-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Купленные товары'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sum',
            field=models.IntegerField(default=0, verbose_name='Остаток товаров'),
        ),
    ]
