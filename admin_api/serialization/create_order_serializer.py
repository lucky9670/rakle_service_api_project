from rest_framework import serializers
from admin_api.models import OrderAcceptance, Order
from app_login.serials.vender_serilizer import VenderSerializer
from app_login.serials.customer_serializer import CustomerSerializer
from admin_api.serialization.get_order_customer_serial import CustomerOrderSerializer

class CreatedOrderSerialiser(serializers.ModelSerializer):
    vender = VenderSerializer(read_only = True)
    customer = CustomerSerializer(read_only = True)
    order = CustomerOrderSerializer(read_only = True)
    class Meta:
        model = OrderAcceptance
        fields = "__all__"

class VenderFilterSerials(serializers.Serializer):
    vender_id = serializers.IntegerField(required=True)

class CustomerFilterSerials(serializers.Serializer):
    customer_id = serializers.IntegerField(required=True)