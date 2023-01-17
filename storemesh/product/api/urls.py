from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( 
   ProductViewSet 
)


app_name="api"
# Create a router and register our viewsets with it.
router = DefaultRouter()
# The API URLs are now determined automatically by the router.
urlpatterns = [
]

router.register(r'product',ProductViewSet,basename="product")


urlpatterns += router.urls



