from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( 
   ProductListView 
)


app_name="api"
# Create a router and register our viewsets with it.
router = DefaultRouter()
# The API URLs are now determined automatically by the router.
urlpatterns = [
   

]

product_url_patterns = [
   path(r'product/',ProductListView.as_view(),name='product-list'),

]


urlpatterns += router.urls
urlpatterns+=product_url_patterns


