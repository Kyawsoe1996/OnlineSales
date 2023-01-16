from urllib import request
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import permissions,generics
from rest_framework import viewsets
from product.models import Product
from .serializers import (
               ProductSerializer
                )
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



# Create your views here.







        
        
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset=Category.objects.all()       
#     serializer_class = CategorySerializer


#     def get_serializer_class(self):
#         print(self.action,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
#         if self.action == 'list':
            
#             return CategorySerializer
#         return CategoryImageUploadableSerializer
    

#     def perform_create(self, serializer):
#         print(self,"######",serializer)
#         print(self.request.data,"#########")
#         business_id = self.request.data.get('business_id',None)
#         print(business_id,'###3')
#         if business_id:
#             try:
#                 business_object= get_object_or_404(Business,pk=int(business_id))
#                 return serializer.save(business_id=business_object)
#             except Exception as e:
#                 raise serializers.ValidationError({"error":"The provide business is not in the database"})
#         else:
#             raise serializers.ValidationError({"error":"Provide Business Id for creating category "})
#     @action(detail=True,methods=['get'])
#     def items(self,request,pk=None):
#         category = self.get_object()
#         items =category.items.all()
        
#         serializer = ItemSerializer(items,many=True)
        
#         return Response(serializer.data,status=status.HTTP_200_OK)

        

# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

