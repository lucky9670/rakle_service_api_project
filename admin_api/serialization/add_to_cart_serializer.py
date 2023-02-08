from rest_framework import serializers
from admin_api.models import AddToCart

class AddToCartSerializer(serializers.ModelSerializer):
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