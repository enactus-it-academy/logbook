# Generated by Django 3.1.7 on 2021-04-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20210408_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_earns',
            field=models.IntegerField(default=0, editable=False, verbose_name='Итоги'),
        ),
        migrations.AlterField(
            model_name='product',
            name='earns_example',
            field=models.IntegerField(default=0, editable=False, verbose_name='Выручка с товара'),
        ),
    ]
