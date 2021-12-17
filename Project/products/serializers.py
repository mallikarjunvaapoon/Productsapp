from rest_framework import serializers
from .models import Brands, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


