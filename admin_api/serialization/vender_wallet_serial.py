from rest_framework import serializers
from admin_api.models import VenderWallet

class VenderWalletSerial(serializers.ModelSerializer):
    class Meta:
        model = VenderWallet
        fields= "__all__"

class VenderWalletInputSerial(serializers.Serializer):
    vender = serializers.IntegerField(required=True)
    order = serializers.IntegerField(required=True)
    amount = serializers.IntegerField(required=True)