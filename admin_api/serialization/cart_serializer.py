from rest_framework import serializers
from admin_api.models import Cart

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

class CartUserSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    user_device_id = serializers.IntegerField(required=False)