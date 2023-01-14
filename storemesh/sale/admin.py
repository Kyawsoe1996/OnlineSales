from django.contrib import admin

# Register your models here.
from .models import SaleOrder,SaleOrderLine

admin.site.register(SaleOrder)
admin.site.register(SaleOrderLine)