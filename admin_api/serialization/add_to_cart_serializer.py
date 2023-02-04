from rest_framework import serializers
from admin_api.models import AddToCart

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields= "__all__" 
