from rest_framework import serializers
from admin_api.serialization.service_serializer import ServiceSerializer
from admin_api.models import AddToCart

class AddToCartSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only = True)
    class Meta:
        model = AddToCart
        fields= "__all__" 
class CustomAddToCart(serializers.ModelSerializer):
    user=serializers.IntegerField(required=False)
    user_device_id= serializers.IntegerField(required=False)
    class Meta:
        model=AddToCart
        fields=('user','user_device_id',)
        depth = 1

class RequiredFieldForATC(serializers.ModelSerializer):
    user=serializers.IntegerField(required=False)
    user_device_id = serializers.IntegerField(required=False)
    service_quantity = serializers.CharField(required=True)
    service_amount = serializers.FloatField(required=True)
    service = serializers.IntegerField(required=True)

    class Meta:
        model=AddToCart
        fields="__all__"
        depth = 1