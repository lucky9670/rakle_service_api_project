from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from app_login.serials.customer_serializer import AllCustomerSerializer, CustomerLoginSerialization, CustomerOTPSerialization, CustomerUpdateSerialization, CustomerSerializer
import random
from drf_yasg.utils import swagger_auto_schema
from app_login.models import AllCustomer
from django.http import JsonResponse

class CustomerGetView(GenericAPIView):
    serializer_class = CustomerSerializer

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['get'])
    def get(self,request):
        try:
            obj=AllCustomer.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','customer':CustomerSerializer(obj,many=True).data},safe=False)

class CustomerOneView(ViewSet):
    serializer_class = CustomerSerializer
    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['get'])
    def get_customer(self,request,id):
        service1 = AllCustomer.objects.get(id=id)
        if not service1: 
            return JsonResponse({'result':"false",'response':"no data present"},safe=False)
        return JsonResponse({'result':"true",'customer':CustomerSerializer(service1).data},safe=False)

class CustomerView(GenericAPIView):
    serializer_class = CustomerLoginSerialization

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        data = request.data
        phone = data["phone"]
        otp = random.randint(1000, 9999)
        try:
            user = AllCustomer.objects.get(phone=phone)
        except:
            user = None
        if user == None:
            user = AllCustomer.objects.create(phone=phone, otp = otp)
            return Response({"status": True, "response": f"OTP send on {phone} number"})
        else:
            user.otp = otp
            user.save()
            return Response({"status": True, "response": f"OTP send on {phone} number"})
    
    
class CustomerLoginView(GenericAPIView):
    serializer_class = CustomerOTPSerialization

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        data = request.data
        phone = data["phone"]
        otp = data["otp"]
        try:
            user = AllCustomer.objects.get(phone=phone)
        except:
            return Response({"status": True, "response": f"Phone Number does not exist"})
        print(user)
        if user.otp == otp:
            context = {
                "id" : user.id,
                "phone" : user.phone,
                "name" : user.name,
                "gender" : user.gender
            }
            return Response({'result':"Success",
                "response": context,
            })
        else:
            return Response({"status": False, "response": f"Invalid OTP"})

class CustomerUpdateView(GenericAPIView):
    serializer_class = AllCustomerSerializer

    @swagger_auto_schema(tags=['Customer Login System'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):
        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        serializer = self.get_serializer(data=check_data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "Cat": CustomerUpdateSerialization(plan, context=self.get_serializer_context()).data,
        })
    
