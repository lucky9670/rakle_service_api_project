from rest_framework import serializers
from admin_api.models import VendorCallSupport

class VendorCallSupportSerial(serializers.ModelSerializer):
    class Meta:
        model =  VendorCallSupport
        fields = "__all__"