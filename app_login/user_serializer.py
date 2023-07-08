from rest_framework import serializers
from .models import UserSignupModel, VenderProfile
from django.contrib.auth import authenticate

class ResiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignupModel
        fields = ('id','name','franchiser', 'role', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = UserSignupModel.objects.create_user(username=validated_data['phone'],phone=validated_data['phone'], password=validated_data['password'],name=validated_data['name'],role=validated_data['role'],  franchiser = validated_data['franchiser'])
        if validated_data['role'] == 3:
            VenderProfile.objects.create(user=user)
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