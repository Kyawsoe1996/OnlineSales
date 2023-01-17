# from inventory.models import Stock

from django.db import models

from django.shortcuts import reverse

from io import BytesIO
from django.core.files import File
from customer.models import Customer
from urllib.parse import urljoin
from django.conf import settings

# Create your models here.

TYPE = (
    ('stock', 'Stockable Product'),
    ('consu', 'Consumable'),
    ('service', 'Service')
    
)

class ProductCategory(models.Model):
    
    name = models.CharField(max_length=50)
    
    class Meta:
        

        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE,default='stock',max_length=10)
    category = models.ForeignKey(ProductCategory,related_name="products",on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField()
    slug = models.SlugField()
    unit_price = models.FloatField(blank=True,null=True)
    description = models.TextField()
    ##TODO###
    qty_in_warehouse_stocks = models.IntegerField(blank=True,null=True)
    #####

    class Meta:
        

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
       return self.name
    #in API, showing url full backend
    @property
    def get_file_url(self):
        
        return urljoin(settings.BACKEND_URL, self.image.url)
    
    # def get_absolute_url(self):
        
    #     return reverse('product:product-detail', kwargs={'id': self.id})


