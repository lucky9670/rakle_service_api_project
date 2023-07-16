from rest_framework.viewsets import ViewSet
from admin_api.serialization.create_order_serializer import CreatedOrderSerialiser
from admin_api.serialization.get_order_customer_serial import CustomerOrderSerializer
from admin_api.models import OrderAcceptance, Order
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from app_login.models import UserSignupModel, AllCustomer

class CreatedOrderView(ViewSet):
    serializer_class = CreatedOrderSerialiser
    queryset = Order.objects.all()

    @swagger_auto_schema(tags=['Order API'])
    def list(self, request):
        serializer = CustomerOrderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['Order API'])
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = CustomerOrderSerializer(item)
        return Response(serializer.data)

class OrderGetView(ViewSet):
    queryset = OrderAcceptance.objects.all()
    
    @action(detail=False, methods=['get'])
    def get_order_basis_of_vender(self, request, id=None):
        vender = UserSignupModel.objects.get(id = id)
        order = OrderAcceptance.objects.filter(vender=vender)
        serializer = CreatedOrderSerialiser(order, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_order_basis_of_customer(self, request, id=None):
        customer = AllCustomer.objects.get(id = id)
        order = OrderAcceptance.objects.filter(customer=customer)
        serializer = CreatedOrderSerialiser(order, many=True)
        return Response(serializer.data)
    