from rest_framework import serializers
from app_login.models import AllCustomer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCustomer
        fields = "__all__"

class AllCustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    email = serializers.CharField(required=False)

class CustomerImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=True)

class CustomerUpdateSerialization(serializers.Serializer):
    # phone = serializers.CharField(required=True)
    class Meta:
        model=AllCustomer
        fields= "__all__"
class CustomerLoginSerialization(serializers.Serializer):
    phone = serializers.CharField(required=True)
    # class Meta:
    #     model=AllCustomer
    #     fields= ("phone", )



class CustomerOTPSerialization(serializers.Serializer):
    phone = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)
    # class Meta:
    #     model=AllCustomer
    #     fields= ("phone", "otp")
