from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from product.models import Product,ProductCategory
from django.http import JsonResponse


class ProductImageUploadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','type','category','image','slug','unit_price','description')

    #if category is blank, creat one, otherwise based on user provided
    def create(self, validated_data):
       
        category = validated_data.get('category',None)
        if category:
            category = validated_data.update({'category':category})
        else:
            categories = ProductCategory.objects.all()
            if categories.exists():
                category = ProductCategory.objects.first()
                category = validated_data.update({'category':category})
            else:
                category = ProductCategory.objects.create(name='Category Test')
                category = validated_data.update({'category':category})

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
        
    

    

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="get_file_url")
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Product
        fields = ('id','name','type','category','image','slug','unit_price','description','qty_in_warehouse_stocks')

    







