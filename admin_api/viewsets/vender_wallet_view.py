from rest_framework.viewsets import ViewSet
from admin_api.models import VenderWallet, Order, OrderAcceptance
from admin_api.serialization.vender_wallet_serial import VenderWalletSerial, VenderWalletInputSerial
from rest_framework.response import Response
from rest_framework import status
from app_login.models import VenderProfile, UserSignupModel
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

@swagger_auto_schema(tags=['Wallet Section'])
class VenderWalletView(ViewSet):
    serializer_class = VenderWalletSerial

    @swagger_auto_schema(tags=['Wallet Section'], request_body=VenderWalletInputSerial)
    def create(self, request):
        data = request.data
        order_id = data['order']
        vender_id = data['vender']
        amount = data['amount']
        oredr_acceptance = OrderAcceptance.objects.get(order = order_id)
        vender = UserSignupModel.objects.get(id = vender_id)
        vender_profile = VenderProfile.objects.get(user = vender)
        print(request.data)
        total_amount = vender_profile.amount + amount*15/100
        vender_profile.amount = total_amount
        vender_profile.save()
        oredr_acceptance.oredr_status = 4
        oredr_acceptance.save()
        serializer = VenderWalletSerial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response ={
            'id': serializer.data['id'], 
            'amount': serializer.data["amount"], 
            'order': serializer.data['order'], 
            'vender': serializer.data['vender'],
            'total_amount': total_amount
        }
        print(response)
        return Response(response, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(tags=['Wallet Section'])
    def retrieve(self, request, pk=None):
        queryset = VenderWallet.objects.filter(vender=pk)
        serializer = VenderWalletSerial(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(tags=['Wallet Section'])
    def list(self, request):
        queryset = VenderWallet.objects.all()
        serializer = VenderWalletSerial(queryset, many=True)
        return Response(serializer.data)