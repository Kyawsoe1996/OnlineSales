from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from product.models import Product
from django.http import JsonResponse


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="get_file_url")
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Product
        fields = ('id','name','type','category','image','slug','unit_price','description')

    







