from admin_api.serialization.address_serializer import AddressSerializer, UserAddressSerials
from admin_api.models import Address, AllCustomer
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class AddressView(ModelViewSet):
    serializer_class = AddressSerializer

    @swagger_auto_schema(tags=['Address View'])
    def get_queryset(self):
        return Address.objects.all()

    @swagger_auto_schema(tags=['Address View'], query_serializer=UserAddressSerials)
    @action(detail=False, methods=['GET'])
    def user_address_list(self, request, *args, **kwargs):
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers, data=serializer.data)
