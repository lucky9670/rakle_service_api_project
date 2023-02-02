from knox.models import AuthToken
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from admin_api.serialization.work_serializer import *
from rackle import settings
from admin_api.models import *
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.utils import timezone
from admin_api.serialization.update_serializer import *
from admin_api.serialization.paymentserializer import *
from rest_framework.parsers import MultiPartParser, FormParser
import razorpay



class PaymentGateway(GenericAPIView):
    serializer_class = OrderSerializer
   
    @swagger_auto_schema(tags=['Order'])
    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        client = razorpay.Client(auth=(settings.razorpay_api_key, settings.razorpay_api_secret_key))

        # try:
        check_data = request.data
        # print(check_data)
        amount = check_data['amount']
        currancy = check_data['currancy']
        # payment_capture = check_data['payment_capture']
        file_serializer = OrderSerializer(data=request.data)
        data1 = client.order.create({"amount": amount*100, "currency": currancy, "payment_capture": 1})
        
        
        return Response({
            "offer": data1,
        })

class Checkout(GenericAPIView):
    serializer_class = CheckoutSerializer
   
    @swagger_auto_schema(tags=['Order'])
    def post(self, request, *args, **kwargs):
        client = razorpay.Client(auth=(settings.razorpay_api_key, settings.razorpay_api_secret_key))
        check_data = request.data
        print(check_data)
        return Response({
            "offer": check_data,
        })