from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Customer

@receiver(user_logged_in)
def create_customer(sender, request, user, **kwargs):
        data  = {"user":user,"username":user.username,"email":user.email,"address":"Default Address"}
        customer = Customer.objects.filter(user=user)
        if customer.exists():
            login(request,user)
        else:
            customer = Customer.objects.create(**data)
            customer.is_buyer = True
            customer.save()
            login(request,user)

    
