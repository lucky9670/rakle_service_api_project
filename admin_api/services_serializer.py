from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = "__all__"

class AboutServiceSerializer(serializers.ModelSerializer):
    # service_name = ServiceSerializer()
    # package = PackageSerializer()
    # faq = ServiceFAQSerializer()
    class Meta:
        model = AboutService
        fields = "__all__"

class AboutServiceSerializerother(serializers.ModelSerializer):
    class Meta:
        model = AboutService
        fields = "__all__"

class Update_MainCat_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    #updated_on= serializers.DateTimeField(input_formats="%Y-%m-%d %H:%M:%S",format="%Y-%m-%d %H:%M:%S", required=True)
    # user_profile=serializers.IntegerField()

    class Meta:
        model=MainCategory
        fields=('id','main_cat_name','status','main_cat_image')

class Update_Cat_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=Category
        fields=('id','main_cat_name','cat_name','status','cat_image')

class Update_MainSer_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=MainService
        fields=('id','main_cat_name','cat_name','main_service_name','status','main_service_image')

class Update_Service_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=Service
        fields=('id','main_cat_name','cat_name','main_service_name','service_name','status',
            'service_image','service_charge','service_time', 'discount')

class Update_ServiceAbout_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=AboutService
        fields=('id','service_name','title','image',
            'video','discription','notes')

class SliderSerializer(serializers.ModelSerializer):
    image=serializers.FileField()
    text=serializers.CharField(required=True)

class SliderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields= "__all__"