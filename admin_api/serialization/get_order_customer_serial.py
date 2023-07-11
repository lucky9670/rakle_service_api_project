from rest_framework import serializers
from admin_api.models import Order
from app_login.serials.customer_serializer import CustomerSerializer
from admin_api.serialization.address_serializer import AddressSerializer
from admin_api.serialization.add_to_cart_serializer import AddToCartSerializer

class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only = True)
    address = AddressSerializer(read_only = True)
    cart_detail = AddToCartSerializer(read_only = True)
    class Meta:
        model = Order
        fields = "__all__"

class OrderByCustomerIDSerializer(serializers.Serializer):
    id = serializers.IntegerField()