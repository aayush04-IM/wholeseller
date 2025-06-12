from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, Product, Sales
from .serializers import CitySerializer, ProductSerializer, SalesSerializer

class CityListView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class SalesListView(APIView):
    def get(self, request):
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data)
