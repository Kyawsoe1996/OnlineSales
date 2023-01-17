from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
# Create your views here.
#customer index page
# @login_required
def customer_index(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request,'customer/index.html',context=context)