# Generated by Django 3.1.7 on 2021-04-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20210407_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='earns_example',
            field=models.IntegerField(default=0, editable=False, verbose_name='Выручка'),
        ),
    ]