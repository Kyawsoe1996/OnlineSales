from django.urls import path,include
from .views import(
        SaleOrderCreate,
        SaleListView,
        SaleDetailView,
        SaleUpdateView,
       

) 

app_name="sale"

urlpatterns = [
    
    path("",SaleOrderCreate.as_view(),name="sale-order"),
    path("list/",SaleListView,name="sale-list"),
    path("detail/<int:pk>/",SaleDetailView.as_view(),name="sale-detail"),
    path("update/<int:pk>/",SaleUpdateView.as_view(),name="sale-update"),
 
]