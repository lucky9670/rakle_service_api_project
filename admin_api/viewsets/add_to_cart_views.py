from rest_framework.response import Response
from admin_api.models import AddToCart,Cart
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from admin_api.serialization.add_to_cart_serializer import AddToCartSerializer, CustomAddToCart, RequiredFieldForATC
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from app_login.models import CustomerDevice, AllCustomer
from admin_api.models import Service
from rest_framework.decorators import action

class AddToCartView(ModelViewSet):
    serializer_class = AddToCartSerializer

    @swagger_auto_schema(tags=["Add To Cart"])
    def get_queryset(self):
        return AddToCart.objects.all()
    
    @swagger_auto_schema(tags=["Add To Cart"], request_body=CustomAddToCart)
    @action(detail=False, methods=['post'])
    def get_cart_item(self, request, *args, **kwargs):
        data = request.data
        try:
            if data.get("user") is not None:
                cart = Cart.objects.get(user=data['user'])
            else:
                cart = Cart.objects.get(user_device_id=data['user_device_id'])
            queryset = self.filter_queryset(AddToCart.objects.filter(cart = cart, checkouted=False))
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"response":"Card is Empaty"})

    @swagger_auto_schema(tags=["Add To Cart"], request_body=RequiredFieldForATC)
    def create(self, request, *args, **kwargs):
        data = request.data
        service = Service.objects.get(id = int(data['service']))
        if data.get('user') !=None or data.get('user')!='':
            user = AllCustomer.objects.get(id = int(data['user']))
            try:
                cart = Cart.objects.get(user=user)
            except:
                cart = Cart.objects.create(user=user)
            try:
                add_to_cart = AddToCart.objects.get(user=user, service = service)
            except:
                add_to_cart = None
            if add_to_cart is not None:
                if int(data['service_quantity']) !=0:
                    add_to_cart.service_quantity = data['service_quantity']
                    add_to_cart.service_amount = data['service_amount']
                    add_to_cart.save()
                else:
                    add_to_cart.delete()
                    return JsonResponse({'status': 'Success', 'message': 'Service Quantity is empaty'}, safe=False)
            else:
                add_to_cart = AddToCart.objects.create(user=user, service = service, service_amount=data['service_amount'], service_quantity=data['service_quantity'], cart=cart)
            serializer = self.get_serializer(add_to_cart)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            user_device = CustomerDevice.objects.get(id = int(data['user_device_id']))
            try:
                cart = Cart.objects.get(user_device=user_device)
            except:
                cart = Cart.objects.create(user_device=user_device)
            try:
                add_to_cart = AddToCart.objects.get(user_device_id=user_device, service = service)
            except:
                add_to_cart = None
            if add_to_cart is not None:
                add_to_cart.service_quantity = data['service_quantity']
                add_to_cart.service_amount = data['service_amount']
                add_to_cart.save()
            else:
                add_to_cart = AddToCart.objects.create(user_device_id=user_device, service = service, service_amount=data['service_amount'], service_quantity=data['service_quantity'], cart=cart)
            serializer = self.get_serializer(add_to_cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # @swagger_auto_schema(tags=["Add To Cart"], request_body=CustomAddToCart)
    # @action(detail=False, methods=['post'])
    # def get_add_to_cart_on_user(self, request, *args, **kwargs):
    #     data = request.data
    #     if data.get('user'):
    #         user = AllCustomer.objects.get(id = int(data['user']))
    #         queryset = AddToCart.objects.filter(user=user)
    #     else:
    #         queryset = AddToCart.objects.filter(user=request.data['user_device_id'])
    #     # queryset = self.filter_queryset(AddToCart.objects_deleted.all())
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)