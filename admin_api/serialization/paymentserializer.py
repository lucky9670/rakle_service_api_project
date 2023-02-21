from rest_framework import serializers
from admin_api.models import Order
from django.contrib.auth import authenticate

class OrderSerializer(serializers.Serializer):
    address = serializers.IntegerField(required = True)
    customer = serializers.IntegerField(required = True)
    cart_detail = serializers.IntegerField(required = True)
    total_amount = serializers.FloatField(required = True)
    delivery_date = serializers.CharField(required = True)
    time_slot = serializers.CharField(required = True)

    # class Meta:
    #     model = Order
    #     fields = "__all__"

class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    amount = serializers.IntegerField()
    currancy = serializers.CharField(max_length=500)
    order_id = serializers.CharField(max_length=300)

