from admin_api.serialization.address_serializer import AddressSerializer
from admin_api.models import Address, AllCustomer
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

class AddressView(ModelViewSet):
    serializer_class = AddressSerializer

    @swagger_auto_schema(tags=['Address View'])
    def get_queryset(self):
        return Address.objects.all()

    @swagger_auto_schema(tags=['Address View'])
    def list(self, request, *args, **kwargs):
        user = AllCustomer.objects.get(id=int(self.request.query_params["user"]))
        queryset = self.filter_queryset(Address.objects.filter(user = user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(tags=['Address View'])
    def create(self, request, *args, **kwargs):
        # data = request.data 
        # longitude = data['longitude']
        # latitude = data['latitude']
        # appartment = data['appartment']
        # address = data['address']
        # flat_no = data['flat_no']
        # save_as = data['save_as']
        # user = data['user']
        # address = 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
