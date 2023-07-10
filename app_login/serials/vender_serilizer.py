from rest_framework import serializers
from app_login.models import VenderProfile
from app_login.user_serializer import ResiterSerializer


class BankUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = ['user',"aadhar_card", 'pan_card', 'account_number', 'ifsc_code', 'account_holder', 'bank_name', 'branch']

class BasicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = ["user","address", 'latitude', 'longitude', 'qualification', 'age', 'gender', 'notification_id', 'email', 'amount', 'no_of_vender']

class ProfilePictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = ["user","image"]

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = ["user","image"]

class VenderSerializer(serializers.ModelSerializer):
    user = ResiterSerializer(read_only = True)
    class Meta:
        model = VenderProfile
        fields = "__all__"


