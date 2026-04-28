from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrReadOnly

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
    permission_classes = [IsSuperUserOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsSuperUserOrReadOnly]