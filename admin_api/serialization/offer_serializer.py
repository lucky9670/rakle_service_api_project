from rest_framework import serializers
from admin_api.models import BestOffer

class BestOfferSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True)
    offer=serializers.CharField(required=True)
    offerimage=serializers.FileField()



class BestOfferGetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    offerimage = serializers.FileField()

    class Meta:
        model = BestOffer
        fields= "__all__"

