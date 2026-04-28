from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'email']

class ProductSerializer(serializers.ModelSerializer):
    imageURL = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'digital', 'image', 'imageURL']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )
    get_total = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'order', 'quantity', 'get_total', 'date_added']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True, read_only=True)
    get_cart_total = serializers.ReadOnlyField()
    get_cart_items = serializers.ReadOnlyField()
    shipping = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'date_ordered',
            'complete',
            'transaction_id',
            'orderitem_set',
            'get_cart_total',
            'get_cart_items',
            'shipping'
        ]

class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = '__all__'
        