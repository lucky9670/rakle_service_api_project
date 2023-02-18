from rest_framework import serializers
from admin_api.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=False)
    user_device_id = serializers.IntegerField(required=False)
    class Meta:
        model = Service
        fields = "__all__"
class ServiceSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"