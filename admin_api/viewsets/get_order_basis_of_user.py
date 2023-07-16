from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from admin_api.serialization.get_order_customer_serial import CustomerOrderSerializer, OrderByCustomerIDSerializer
from admin_api.models import Order
from rest_framework import status

class CustomerOrderGetView(ViewSet):
    def get(self, request, id=None):
        if id:
            queryset = Order.objects.filter(customer=id)
            order = queryset.get(pk=id)
            serializer = CustomerOrderSerializer(order)
            return Response(serializer.data)
        return Response({'detail': 'Customer ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)