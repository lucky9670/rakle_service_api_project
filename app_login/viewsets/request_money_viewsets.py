from rest_framework.viewsets import ViewSet
from admin_api.models import FranchieserRequestMoney, VendorRequestMoney    
from app_login.models import UserSignupModel, VenderProfile, FranchieserProfile    
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from app_login.serials.request_money_serial import VenderRequestMoneySerial,  FranchieserRequestMoneySerial, VenderAcceptMoneySerial, VenderGetRequestMoneySerial, FranchaiserAcceptMoneySerial, FranchieserGetRequestMoneySerial
from django.http import JsonResponse
from rest_framework.response import Response

@swagger_auto_schema(tags=['Request Vender Money'])
class VenderRequestMoneyViews(ViewSet):
    @swagger_auto_schema(tags=['Request Vender Money'], request_body=VenderRequestMoneySerial)
    @action(detail=False, methods=['post'])
    def vender_money_request(self, request):
        data = request.data
        vender = VenderProfile.objects.get(user=data['vender_id'])
        if data['requested_amount'] <= vender.amount:
            print(vender.amount-data['requested_amount'])
            VendorRequestMoney.objects.create(vendor=UserSignupModel.objects.get(id=data['vender_id']), amount=data['requested_amount'], notes=data['notes'])
            return JsonResponse({'status': True, "massage": "Your Request Amount send tothe admin"})
        else:
            return JsonResponse({'status': False, "massage": "Your amount is Low"})
    
    @swagger_auto_schema(tags=['Request Vender Money'], request_body=VenderAcceptMoneySerial)
    @action(detail=False, methods=['post'])
    def accept_vender_money(self, request):
        data = request.data
        vender_request = VendorRequestMoney.objects.get(id = data['vender_request_money_id'])
        vender = VenderProfile.objects.get(user=vender_request.vendor.id)
        vender.amount = vender.amount - vender_request.amount
        vender.save()
        vender_request.status = True
        vender_request.save()
        return JsonResponse({'status': True, "massage": "Amount is credit to vender Account"})

    @swagger_auto_schema(tags=['Request Vender Money'])
    def retrieve(self, request, pk=None):
        queryset = VendorRequestMoney.objects.filter(vendor=pk)
        serializer = VenderGetRequestMoneySerial(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(tags=['Request Vender Money'])
    def list(self, request):
        queryset = VendorRequestMoney.objects.all()
        serializer = VenderGetRequestMoneySerial(queryset, many=True)
        return Response(serializer.data)

@swagger_auto_schema(tags=['Request Franchaiser Money'])
class FanchaiserRequestMoneyViews(ViewSet):
    @swagger_auto_schema(tags=['Request Franchaiser Money'], request_body=FranchieserRequestMoneySerial)
    @action(detail=False, methods=['post'])
    def francheiser_money_request(self, request):
        data = request.data
        vender = FranchieserProfile.objects.get(user=data['franchieser_id'])
        if data['requested_amount'] <= vender.amount:
            print(vender.amount-data['requested_amount'])
            FranchieserRequestMoney.objects.create(franchiser=UserSignupModel.objects.get(id=data['franchieser_id']), amount=data['requested_amount'], notes=data['notes'])
            return JsonResponse({'status': True, "massage": "Your Request Amount send tothe admin"})
        else:
            return JsonResponse({'status': False, "massage": "Your amount is Low"})
    
    @swagger_auto_schema(tags=['Request Franchaiser Money'], request_body=FranchaiserAcceptMoneySerial)
    @action(detail=False, methods=['post'])
    def accept_franchaiser_money(self, request):
        data = request.data
        vender_request = FranchieserRequestMoney.objects.get(id = data['franchaiser_request_money_id'])
        vender = FranchieserProfile.objects.get(user=vender_request.franchiser.id)
        vender.amount = vender.amount - vender_request.amount
        vender.save()
        vender_request.status = True
        vender_request.save()
        return JsonResponse({'status': True, "massage": "Amount is credit to vender Account"})

    @swagger_auto_schema(tags=['Request Franchaiser Money'])
    def retrieve(self, request, pk=None):
        queryset = FranchieserRequestMoney.objects.filter(franchiser=pk)
        serializer = FranchieserGetRequestMoneySerial(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(tags=['Request Franchaiser Money'])
    def list(self, request):
        queryset = FranchieserRequestMoney.objects.all()
        serializer = FranchieserGetRequestMoneySerial(queryset, many=True)
        return Response(serializer.data)