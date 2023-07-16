from rest_framework import serializers
from admin_api.models import WhyService

class WhyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyService
        fields= "__all__"