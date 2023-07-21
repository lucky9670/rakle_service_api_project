from rest_framework import serializers
from .models import UserSignupModel, VenderProfile, FranchieserProfile
from django.contrib.auth import authenticate
from fcm_django.models import FCMDevice

class ResiterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True, required = True)
    class Meta:
        model = UserSignupModel
        fields = ('id','name','franchiser', 'role', 'phone', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = UserSignupModel.objects.create_user(username=validated_data['phone'],phone=validated_data['phone'], password=validated_data['password'],name=validated_data['name'],role=validated_data['role'],  franchiser = validated_data['franchiser'])
        if validated_data['role'] == 3:
            vender_obj = VenderProfile.objects.create(user=user, notification_id = validated_data['token'])
            ofcdevice_obj = FCMDevice.objects.filter(registration_id=validated_data['token'], user=user)
            if not ofcdevice_obj:
                FCMDevice.objects.create(registration_id=validated_data['token'], type="android", user=user)
            
        if validated_data['role'] == 2:
            FranchieserProfile.objects.create(user=user)
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignupModel
        fields = ( 'phone', 'password')

class UserLoginSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )
    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data
    
class ChangePasswordSerial(serializers.ModelSerializer):
    #email=serializers.EmailField(max_length=30)
    currentpassword=serializers.CharField(max_length=30)
    new_password=serializers.CharField(max_length=30,min_length=4)
    confirmpassword=serializers.CharField(max_length=20,min_length=4)
    
    class Meta:
        model = UserSignupModel
        fields = ['currentpassword','new_password','confirmpassword']
    

class ForgetPasswordSerial(serializers.ModelSerializer):
    phone=serializers.CharField(max_length=30)
    class Meta:
        model = UserSignupModel
        fields = ['phone']

class ResetPasswordSerial(serializers.ModelSerializer):
    new_password=serializers.CharField(max_length=30,min_length=4)
    confirm_password=serializers.CharField(max_length=20,min_length=4)
    phone=serializers.CharField(max_length=20,min_length=4)
    otp=serializers.CharField(max_length=20,min_length=4)
    
    class Meta:
        model = UserSignupModel
        fields = ['new_password','confirm_password', 'phone', 'otp']