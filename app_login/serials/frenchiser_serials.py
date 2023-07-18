from rest_framework import serializers
from app_login.models import FranchieserProfile
from app_login.user_serializer import ResiterSerializer


class FranchieserBankUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchieserProfile
        fields = "__all__"

class FranchieserBasicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchieserProfile
        fields = "__all__"

class FranchieserProfilePictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchieserProfile
        fields = ["user","image"]

class FranchieserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchieserProfile
        fields = ["user","image"]

class FranchieserFrenchiserSerializer(serializers.ModelSerializer):
    user = ResiterSerializer(read_only = True)
    class Meta:
        model = FranchieserProfile
        fields = "__all__"


