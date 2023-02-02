from rest_framework import serializers
from admin_api.models import *
from django.contrib.auth import authenticate

class OrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    # status = serializers.BooleanField()
    currancy = serializers.CharField(max_length=500)
    # payment_capture = serializers.CharField(max_length=500)


class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    amount = serializers.IntegerField()
    currancy = serializers.CharField(max_length=500)
    order_id = serializers.CharField(max_length=300)

