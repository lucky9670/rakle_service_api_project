from knox.models import AuthToken
from rest_framework import permissions, status
from django.conf import settings
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .user_serializer import LoginSerializer, UserLoginSerializers, ResiterSerializer
from django.contrib.auth.hashers import make_password
import datetime
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from app_login.models import UserSignupModel
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from datetime import timezone
from knox.auth import TokenAuthentication

def password_check(passwd):
    flag = 0
    import re
    if not re.search("[A-Z]", passwd):
        flag = 1
    if not re.search("[0-9]", passwd):
        flag = 2
    if not re.search("[@$!%*#?&]", passwd):
        flag = 3
    return flag

class RegisterAPI(GenericAPIView):
    serializer_class = ResiterSerializer

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, *args, **kwargs):
        try:
            check_data = request.data
            check_password = check_data['password']
            phone = check_data['phone']
            checkpoint = password_check(check_password)
            if checkpoint == 1:
                return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one capital alphbat'}, safe=False)
            if checkpoint == 2:
                return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one digit'}, safe=False)
            if checkpoint == 3:
                return JsonResponse({'result': 'fail', 'response': 'Password must contains one special character like @, $,#,&'}, safe=False)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Please enter valid password '}, safe=False)
        user_check_obj = UserSignupModel.objects.filter(phone=phone).count()
        if user_check_obj != 0:
            return JsonResponse({'result': 'false', 'response': 'user already exists!'}, safe=False)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": ResiterSerializer(user, context=self.get_serializer_context()).data,
        })

class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, format=None):
        info = request.data
        try:
            phone = info['phone']
            password = info['password']
        except Exception as e:
            return Response({'status': 'Success Fail', 'message': 'PLease enter valid email or password '},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        usercheck = UserSignupModel.objects.filter(phone__iexact=phone).count()
        if usercheck == 0:
            message = {'status': 'Fail',
                       'message': 'Please enter valid email or password! '}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        userdata = UserSignupModel.objects.get(phone__iexact=phone)

        if userdata.check_password(password) and userdata.is_active == True:
            import pytz
            utc_now = datetime.datetime.now(tz=timezone.utc)
            utc_now = utc_now.replace(tzinfo=pytz.utc)
            print("getting user data: ", userdata)
            result = {
                'token':AuthToken.objects.create(user=userdata)[1],
                **ResiterSerializer(userdata, context=self.get_serializer_context()).data
            }
            return JsonResponse({'status': 'Success', 'message': 'You have signin successfully!', 'data': result}, safe=False)
        else:
            message = {'status': 'Fail',
                       'message': 'Please enter valid email or password! '}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

class logout(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request):
        
        AuthToken.objects.filter(user=request.user).delete()
        return Response({'result': 'true', 'response': 'logged out successfully'},status=status.HTTP_200_OK)


# class LoginView(ModelViewSet):
#     serializer_class = UserLoginSerializers
#     permission_classes = (permissions.AllowAny,)

#     @action(detail=False, methods=['post'])
#     def login(self, request, *args, **kwargs):
#         serializer = UserLoginSerializers(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         return Response({
#             "user": LoginSerializer(user).data,
#             "token_jwt": jwt_views.TokenObtainPairView(),
#             # "token_knox": AuthToken.objects.create(user)[1]
#         })

# class SignupView(ModelViewSet):
#     serializer_class = LoginSerializer
#     permission_classes = (permissions.AllowAny,)

#     @action(detail=False, methods=['post'])
#     def signup(self, request):
#         data = request.data.copy()
#         data["password"] = make_password(data["password"])
#         data["email"] = data["email"].lower()
#         serializer = LoginSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": LoginSerializer(user).data,
#             "token_jwt": jwt_views.TokenObtainPairView(),
#             # "token_knox": AuthToken.objects.create(user)[1]
#         })
    
    