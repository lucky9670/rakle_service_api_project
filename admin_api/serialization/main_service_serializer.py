from rest_framework import serializers
from admin_api.models import MainService

class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields = "__all__"