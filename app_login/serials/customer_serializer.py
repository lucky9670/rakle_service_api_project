from rest_framework import serializers
from app_login.models import AllCustomer

class AllCustomerSerializer(serializers.Serializer):
    class Meta:
        model = AllCustomer
        fields = "__all__"
