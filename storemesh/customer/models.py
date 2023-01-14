from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class Customer(models.Model):
    
    user = models.OneToOneField(User,related_name="customer", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    is_buyer = models.BooleanField(default=True)
    is_seller =models.BooleanField(default=False)
    country = CountryField(multiple=False)
    image = models.ImageField()
