from rest_framework import serializers
from admin_api.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)
    class Meta:
        model = Service
        fields = "__all__"