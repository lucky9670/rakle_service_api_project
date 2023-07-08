from rest_framework import serializers
from admin_api.models import Address

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"

class UserAddressSerials(serializers.Serializer):
    user = serializers.IntegerField()