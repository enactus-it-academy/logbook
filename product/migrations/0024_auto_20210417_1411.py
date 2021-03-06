# Generated by Django 3.1.7 on 2021-04-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20210417_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='earns_example',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sum',
        ),
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество купленных товаров'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_earns',
            field=models.IntegerField(default=0, editable=False, verbose_name='Выручка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_count',
            field=models.IntegerField(default=0, editable=False, verbose_name='Остаток товаров'),
        ),
        migrations.AlterField(
            model_name='product',
            name='earns',
            field=models.IntegerField(default=0, editable=False, verbose_name='Выручка с товара'),
        ),
    ]
