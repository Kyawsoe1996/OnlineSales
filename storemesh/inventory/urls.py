from django.urls import path,include
from .views import(
        WarehouseListView,
        WarehouseCreateView,
        WarehouseDetailView,
        WarehouseUpdateView,
        WarehouseDeleteView,
        add_stock_to_warehouse,
        StockListView,
        StockCreateView,
        StockUpdateView,
        StockDetailView,
        StockDeleteView

) 

app_name="inventory"

urlpatterns = [
    
    path("warehouse/list",WarehouseListView.as_view(),name="warehouse-list"),

    path("warehouse/",WarehouseCreateView.as_view(),name="warehouse"),
    path('warehouse/<int:pk>/', WarehouseDetailView.as_view(),name='warehouse-detail'),
    path('warehouse/update/<int:pk>/', WarehouseUpdateView.as_view(),name='warehouse-update'),
    path('warehouse/delete/<int:pk>/', WarehouseDeleteView.as_view(),name='warehouse-delete'),
    path('warehouse/<int:pk>/add-stocks/',add_stock_to_warehouse,name='add-stocks-to-warehouse'),
    path('stock/list/',StockListView.as_view(),name='stock-list'),
    path("stock/",StockCreateView.as_view(),name="stock"),
    path('stock/update/<int:pk>/', StockUpdateView.as_view(),name='stock-update'),
    path('stock/<int:pk>/', StockDetailView.as_view(),name='stock-detail'),
    path('stock/delete/<int:pk>/', StockDeleteView.as_view(),name='stock-delete'),

    
]