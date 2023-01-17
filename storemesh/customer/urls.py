from django.urls import path,include
from .views import (
    customer_index
)
app_name="customer"

urlpatterns = [
   path("",customer_index,name="customer-index"),

    
]
