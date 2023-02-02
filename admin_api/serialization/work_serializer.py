from rest_framework import serializers
from admin_api.models import *
from django.contrib.auth import authenticate

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class BookServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookService
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

    
class PartnerDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerDocument
        fields = "__all__"

class PartnerProffetionalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerProffetionalDetail
        fields = "__all__"

class PartnerWorkBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerWorkBook
        fields = "__all__"

class PartnerAwardAndPhoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerAwardAndPhote
        fields = "__all__"


class PartnerServiceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerServiceLocation
        fields = "__all__"


class PartnerServiceRefrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerServiceRefrence
        fields = "__all__"

class VideoConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoConsultation
        fields = "__all__"


class BestOfferSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True)
    offer=serializers.CharField(required=True)
    offerimage=serializers.FileField()



class BestOfferGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestOffer
        fields= "__all__"



class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields= "__all__"


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields= "__all__" 