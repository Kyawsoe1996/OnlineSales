# Generated by Django 3.2 on 2023-01-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty_in_warehouse_stocks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
