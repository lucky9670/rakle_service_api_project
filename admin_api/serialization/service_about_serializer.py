from rest_framework import serializers
from admin_api.models import AboutService

class AboutServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutService
        fields = "__all__"