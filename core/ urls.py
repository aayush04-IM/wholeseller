from django.urls import path
from .views import CityListView, ProductListView, SalesListView

urlpatterns = [
    path('cities/', CityListView.as_view(), name='city-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('sales/', SalesListView.as_view(), name='sales-list'),
]
