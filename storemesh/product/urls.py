from django.urls import path,include
from .views import (
    ProductCategoryView,
    CategoryList,
    CategoryDetail,
    CategoryDelete,

    ProductView,
    ProductList,
    ProductDetail,
    ProductDelete,
    

    ProductStockDetail,
)
app_name="product"

urlpatterns = [
    path("category/",ProductCategoryView,name="product-category"),
    path("category/list/",CategoryList,name="product-category-list"),
    # path('<int:id>/',ProductCategoryView,"category-update"),
    path('category/<int:id>/', ProductCategoryView,name='category-update'),
    path('category/detail/<int:id>/',CategoryDetail,name="category-detail"),
    path('category/delete/<int:id>/',CategoryDelete,name="category-delete"),

    path("",ProductView,name="product"),
    path("list/",ProductList,name="product-list"),
    path('<int:id>/', ProductView,name='product-update'),
    path('detail/<int:id>/',ProductDetail,name="product-detail"),
    path('delete/<int:id>/',ProductDelete,name="product-delete"),


    path('<int:id>/stock/detail',ProductStockDetail,name="stock-detail")




    

    
    # path("", CustomerView, name="cus"),
    # path('<int:id>/', CustomerView,name='customer-update'),
    # path('list/',Customerlist,name="customer-lists"),
    # path('detail/<int:id>/',CustomerDetail,name="customer-detail"),
    # path('delete/<int:id>/',CustomerDelete,name="customer-delete"),

    
]
