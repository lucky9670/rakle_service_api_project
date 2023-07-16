from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from admin_api.serialization.order_acceptance_serial import OrderAcceptanceData, GetLocationSerial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_login.models import UserSignupModel, AllCustomer, VenderProfile
from admin_api.models import OrderAcceptance, Order
from django.http import JsonResponse

class OrderAcceptanceAPiView(GenericAPIView):
    @swagger_auto_schema(tags=['Order acceptance View'], request_body=OrderAcceptanceData)
    def post(self, request, format=None):
        info = request.data
        try:
            vender_id = info['vender']
            order_id = info['order']
            acceptance = info['acceptance']
        except Exception as e:
            return Response({'status': 'Success Fail', 'message': 'PLease enter valid email or password '},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        vender = UserSignupModel.objects.get(id=vender_id)
        order = Order.objects.get(order_id=order_id)
        order_acceptance = OrderAcceptance.objects.get(order=order)
        customer = AllCustomer.objects.get(id = order_acceptance.customer.id)
        vender_profile = VenderProfile.objects.get(user = vender)
        if acceptance == 1:
            order_acceptance.oredr_status = 1
            order_acceptance.vender = vender
            order_acceptance.save()
            order.delevery_status = 2
            order.save()
            data = {
                "vender_latitude": vender_profile.latitude,
                "vender_longitude": vender_profile.longitude
            }
            return JsonResponse({'status': 'Success', 'data': data}, safe=False)
        return JsonResponse({'status': 'Success', 'massage': "You have reject the order"}, safe=False)
    
@swagger_auto_schema(tags=['Order acceptance View'])
class GetVenderLocationView(ViewSet):

    @swagger_auto_schema(tags=['Order acceptance View'])
    @action(detail=False, methods=['get'])
    def get_vender_location(self, request, id=None):
        vender = UserSignupModel.objects.get(id = id)
        # import pdb;pdb.set_trace()
        vender_profile = VenderProfile.objects.get(user = vender)
        data = {
            "user": vender_profile.user.id,
            "longitude": vender_profile.longitude,
            "latitude": vender_profile.latitude
        }
        return JsonResponse({'status': 'Success', 'massage': data}, safe=False)