from django.db import models
from product.models import Product
# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse,related_name="stocks",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,related_name="stocks",on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.warehouse.name}-{self.product_id.name}-{self.quantity}'

    