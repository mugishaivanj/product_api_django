from rest_framework import serializers
from rest_framework import renderers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model=Product
        fields ='__all__'
        
