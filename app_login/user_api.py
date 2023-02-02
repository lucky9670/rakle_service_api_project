from knox.models import AuthToken
from rest_framework import permissions
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .user_serializer import LoginSerializer, UserLoginSerializers
from django.contrib.auth.hashers import make_password
import datetime
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings


class LoginView(ModelViewSet):
    serializer_class = UserLoginSerializers
    permission_classes = (permissions.AllowAny,)

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        serializer = UserLoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({
            "user": LoginSerializer(user).data,
            "token_jwt": jwt_views.TokenObtainPairView(),
            # "token_knox": AuthToken.objects.create(user)[1]
        })

class SignupView(ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        data = request.data.copy()
        data["password"] = make_password(data["password"])
        data["email"] = data["email"].lower()
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": LoginSerializer(user).data,
            "token_jwt": jwt_views.TokenObtainPairView(),
            # "token_knox": AuthToken.objects.create(user)[1]
        })
    
    