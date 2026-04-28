from rest_framework import viewsets
from .models import Product, Order, OrderItem, Customer, ShippingAddress
from .serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
    CustomerSerializer,
    ShippingAddressSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

