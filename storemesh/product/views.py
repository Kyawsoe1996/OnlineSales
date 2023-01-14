from product.forms import ProductCategroyForm,ProductForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from .forms import ProductCategroyForm
from product.models import Product,ProductCategory
# Create your views here.

#Product Category
def ProductCategoryView(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductCategroyForm()
        else:
            category_obj = ProductCategory.objects.get(pk=id)
            form = ProductCategroyForm(instance=category_obj)    
        return render(request,"product_category/index.html",{"form":form})
    else:
        if id ==0 :
            form = ProductCategroyForm(request.POST)
        else:
            category_obj = ProductCategory.objects.get(pk=id)
            form = ProductCategroyForm(request.POST,instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect("product:product-category-list")
        


def CategoryList(request):
    category_lists =  ProductCategory.objects.all()
    context = {
        "category_lists":category_lists
    }
    return render(request,"product_category/list.html",context)

def CategoryDetail(request,id):
    category_obj = ProductCategory.objects.get(pk=id)

    context = {
        "category":category_obj
    }
    return render(request,"product_category/detail.html",context)

def CategoryDelete(request,id):
    category_obj = ProductCategory.objects.get(pk=id)
    category_obj.delete()
    return redirect("product:product-category-list")

#Product
def ProductView(request,id=0):
    # return render(request,"product/index.html")
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product_obj = Product.objects.get(pk=id)
            form = ProductForm(instance=product_obj)
        return render(request,"product/index.html",{"form":form})
    else:
        if id == 0:
            form = ProductForm(request.POST,request.FILES)
        else:
            product_obj = Product.objects.get(pk=id)
            form = ProductForm(request.POST,request.FILES, instance=product_obj)
        if form.is_valid():
            form.save()
        return redirect("product:product-list")


def ProductList(request):
    product_lists = Product.objects.all()
    context = {
        "product_lists":product_lists
    }

    return render(request,"product/list.html",context)
    

def ProductDetail(request,id):
    try:
        product_obj = Product.objects.get(pk=id)

    except:
        context = {
            "page":"Product Detail",
            "detail":"Product detail can't found"
        }
        return render(request,"page-404.html",context)
   
    context = {
        "product":product_obj,
        
    }

    return render(request,"product/detail.html",context)

def ProductDelete(request,id):
    product_obj = Product.objects.get(pk=id)
    product_obj.delete()
    return redirect("product:product-list")



def ProductStockDetail(request,id):
    product = Product.objects.get(id=id)
    context = {
        "product":product
    }
    
    return render(request,"stock_location_detail/location_detail.html",context)


