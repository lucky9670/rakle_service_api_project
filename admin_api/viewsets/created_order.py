from rest_framework.viewsets import ViewSet
from admin_api.serialization.create_order_serializer import CreatedOrderSerialiser, VenderFilterSerials, CustomerFilterSerials
from admin_api.models import OrderAcceptance
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from app_login.models import UserSignupModel, AllCustomer

class CreatedOrderView(ViewSet):
    serializer_class = CreatedOrderSerialiser
    queryset = OrderAcceptance.objects.all()

    @swagger_auto_schema(tags=['Order API'])
    def list(self, request):
        serializer = CreatedOrderSerialiser(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['Order API'])
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = CreatedOrderSerialiser(item)
        return Response(serializer.data)

class OrderGetView(ViewSet):
    queryset = OrderAcceptance.objects.all()
    
    @action(detail=False, methods=['get'])
    def get_order_basis_of_vender(self, request, id=None):
        vender = UserSignupModel.objects.get(id = id)
        order = get_object_or_404(self.queryset, vender=vender)
        serializer = CreatedOrderSerialiser(order)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_order_basis_of_customer(self, request, id=None):
        customer = AllCustomer.objects.get(id = id)
        order = get_object_or_404(self.queryset, customer=customer)
        serializer = CreatedOrderSerialiser(order)
        return Response(serializer.data)
    