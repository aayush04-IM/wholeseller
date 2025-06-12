from rest_framework import serializers
from .models import City, Product, Sales

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    product = ProductSerializer()

    class Meta:
        model = Sales
        fields = '__all__'
