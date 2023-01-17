from urllib import request
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import permissions,generics
from rest_framework import viewsets
from product.models import Product
from .serializers import (
               ProductSerializer,
               ProductImageUploadableSerializer
                )
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
       
        if self.action == 'list':
            
            return ProductSerializer
        return ProductImageUploadableSerializer

