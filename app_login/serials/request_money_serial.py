from rest_framework import serializers
from admin_api.models import VendorRequestMoney, FranchieserRequestMoney

class VenderRequestMoneySerial(serializers.Serializer):
    vender_id = serializers.IntegerField(required=True)
    requested_amount = serializers.IntegerField(required=True)
    notes = serializers.CharField(required=False)

class VenderGetRequestMoneySerial(serializers.ModelSerializer):
    class Meta:
        model = VendorRequestMoney
        fields = "__all__"

class FranchieserRequestMoneySerial(serializers.Serializer):
    franchieser_id = serializers.IntegerField(required=True)
    requested_amount = serializers.IntegerField(required=True)
    notes = serializers.CharField(required=False)

class VenderAcceptMoneySerial(serializers.Serializer):
    vender_request_money_id = serializers.IntegerField(required=True)

class FranchaiserAcceptMoneySerial(serializers.Serializer):
    franchaiser_request_money_id = serializers.IntegerField(required=True)

class FranchieserGetRequestMoneySerial(serializers.ModelSerializer):
    class Meta:
        model = FranchieserRequestMoney
        fields = "__all__"


