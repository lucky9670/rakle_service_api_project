from rest_framework import serializers

class OrderAcceptanceData(serializers.Serializer):
    vender = serializers.IntegerField(required=True)
    order = serializers.IntegerField(required=True)
    acceptance = serializers.IntegerField(required=True)

class GetLocationSerial(serializers.Serializer):
    vender = serializers.IntegerField(required=True)