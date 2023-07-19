from knox.models import AuthToken
from rest_framework import permissions, status
from django.conf import settings
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .user_serializer import LoginSerializer, ResiterSerializer, ChangePasswordSerial, ForgetPasswordSerial, ResetPasswordSerial
import datetime
from django.conf import settings
from app_login.models import UserSignupModel
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from datetime import timezone
from knox.auth import TokenAuthentication
import random

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
            'result': 'success', "response": ResiterSerializer(user, context=self.get_serializer_context()).data,
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


class ChangePassword(GenericAPIView):
    serializer_class = ChangePasswordSerial
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request):
        message = {'result': '', 'response': ''}
        info = request.data
        try:
            email = request.user.phone
        except Exception as e:
            message['result'] = 'false'
            message['response'] = 'Email not sent please check '
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        try:
            currentpassword = info['currentpassword']
        except Exception as e:
            message['result'] = 'false'
            message['response'] = 'currentpassword  not sent please check '
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        try:
            password = info['new_password']
        except Exception as e:
            message['result'] = 'false'
            message['response'] = 'password not sent please check '
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        try:
            confirmpassword = info['confirmpassword']
        except Exception as e:
            message['result'] = 'false'
            message['response'] = 'confirmpassword not sent please check '
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        if not email:
            message = {'result': 'false', 'response': 'enter valid email data'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        if not currentpassword:
            message = {'result': 'false', 'response': 'enter valid current password'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        if not password:
            message = {'result': 'false', 'response': 'enter valid password data'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        if not confirmpassword:
            message = {'result': 'false', 'response': 'enter valid confirmpassword data'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 4:
            message = {'result': 'false', 'response': 'enter password of minimun 4 digits'}
            return JsonResponse(message, safe=False)

        check_password = password
        checkpoint = password_check(check_password)
        if checkpoint == 1:
            return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one capital alphbat'}, safe=False)
        if checkpoint == 2:
            return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one digit'}, safe=False)
        if checkpoint == 3:
            return JsonResponse({'result': 'fail', 'response': 'Password must contains one special character like @, $,#,&'}, safe=False)

        if password != confirmpassword:
            message = {'result': 'false', 'response': 'password and confirmpassword doesnot match'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        userobj = UserSignupModel.objects.filter(phone=email).count()
        if userobj == 0:
            message = {'result': 'false', 'response': 'Either Email or password doesnot match'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        try:
            userdata = UserSignupModel.objects.get(phone=email)
            if userdata.check_password(password):
                message = {'result': 'false', 'response': 'new password already exists'}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
            if userdata.check_password(currentpassword):
                userdata.set_password(password)
                userdata.save()                
            else:
                message = {'result': 'false', 'response': 'wrong current password'}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {'result': 'false', 'response': 'something went wrong'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        result = AuthToken.objects.filter(user=userdata).delete()
        message = {'result': 'true', 'response': 'successfull changed password'}
        return Response(message,status=status.HTTP_200_OK)

class Forgetpassword(GenericAPIView):
    serializer_class = ForgetPasswordSerial

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request):
        info = request.data
        try:
            email = info['phone']
        except Exception as e:
            return JsonResponse({'result': 'false', 'response': 'Phone not provided','code':status.HTTP_422_UNPROCESSABLE_ENTITY}, safe=False,status=422)

        if not email:
            return JsonResponse({'result': 'false', 'response': 'enter valid data'}, safe=False)

        userobj = UserSignupModel.objects.filter(phone=email).count()
        if userobj == 0:
            return JsonResponse({'result': 'false', 'response': 'Phone does not exist', 'message': 'Given email is invalid please enter valid Phone', 'code': status.HTTP_400_BAD_REQUEST}, safe=False,status=400)
        user = UserSignupModel.objects.get(phone=email)
        otp = random.randint(1000, 9999)
        user.otp = otp
        user.save()
        return JsonResponse({'result': 'true', 'response': f'Validate it from your OTP sent on your phone {otp}'}, safe=False)



class ResetPassword(GenericAPIView):
    serializer_class = ResetPasswordSerial

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request):

        message = {'result': '', 'response': ''}
        info = request.data

        try:
            password = info['new_password']
            conf_password = info['confirm_password']
            phone = info['phone']
            otp = info['otp']
        except Exception as e:
            message['result'] = 'false'
            message['response'] = 'confirm_password or password  not sent please check '
            return JsonResponse(message, safe=False,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not password:
            message = {'result': 'false', 'response': 'enter valid password data'}
            return JsonResponse(message, safe=False,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if not conf_password:
            message = {'result': 'false', 'response': 'enter valid password data'}
            return JsonResponse(message, safe=False,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if len(password) < 4:
            message = {'result': 'false', 'response': 'enter password of minimun 4 digits'}
            return JsonResponse(message, safe=False,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        check_password = password
        checkpoint = password_check(check_password)
        if checkpoint == 1:
            return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one capital alphbat'}, safe=False,status=status.HTTP_400_BAD_REQUEST)
        if checkpoint == 2:
            return JsonResponse({'result': 'fail', 'response': 'Password must contain atleast one digit'}, safe=False,status=status.HTTP_400_BAD_REQUEST)
        if checkpoint == 3:
            return JsonResponse({'result': 'fail', 'response': 'Password must contains one special character like @, $,#,&'}, safe=False,status=status.HTTP_400_BAD_REQUEST)
        if password != conf_password:
            message = {'result': 'false', 'response': 'password doesnot match'}
            return JsonResponse(message, safe=False,status=status.HTTP_400_BAD_REQUEST)
        try:
            userdata = UserSignupModel.objects.get(phone=phone)
            if userdata.otp == otp:
                userdata.set_password(password)
                userdata.save()
                message = {'result': 'true', 'response': 'successfull reseted password'}
                return JsonResponse(message, safe=False)
            else:
                message = {'result': 'false', 'response': 'OTP is invalid'}
                return JsonResponse(message, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            message = {'result': 'false', 'response': 'something went wrong'}
            return JsonResponse(message, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)