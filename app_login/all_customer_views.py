from rest_framework import permissions
from django.conf import settings
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from app_login.serials.customer_serializer import AllCustomerSerializer
import random
from drf_yasg.utils import swagger_auto_schema
from app_login.models import AllCustomer

class CustomerView(GenericAPIView):
    serializer_class = AllCustomerSerializer

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['post'])
    def post(self, request):
        data = request.data
        phone = data["phone"]
        otp = random.randint(1000, 9999)
        print(otp)
        # import pdb;pdb.set_trace()
        try:
            user = AllCustomer.objects.get(phone=phone)
        except:
            user = None
        print(user)
        if user == None:
            user = AllCustomer.objects.create(phone=phone, otp = otp)
            # serializer = AllCustomerSerializer(phone=phone, otp=otp)
            return Response({"status": True, "response": f"OTP send on {phone} number"})
        else:
            user.otp = otp
            user.save()
            return Response({"status": True, "response": f"OTP send on {phone} number"})
    
    
class CustomerLoginView(GenericAPIView):
    serializer_class = AllCustomerSerializer

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['post'])
    def post(self, request):
        data = request.data
        phone = data["phone"]
        otp = data["otp"]
        try:
            user = AllCustomer.objects.get(phone=phone)
        except:
            return Response({"status": True, "response": f"Phone Number does not exist"})
        print(user)
        if user.otp == otp:
            # user = AllCustomer.objects.create(phone=phone, otp = otp)
            # serializer = AllCustomerSerializer(phone=phone, otp=otp)
            return Response({"status": True, "response": f"OTP Varified of {phone} number"})
        else:
            return Response({"status": False, "response": f"Invalid OTP"})
    
    
