from admin_api.models import Cart, AllCustomer
from admin_api.serialization.cart_serializer import CartSerializer, CartUserSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.http import JsonResponse

class CartView(ViewSet):
    serializer_class = CartSerializer

    @swagger_auto_schema(tags=['Category Updated'])
    def get_queryset(self):
        return Cart.objects.all()

    @swagger_auto_schema(tags=['Cart'])
    def list(self, request):
        serializer = CartSerializer(Cart.objects.all(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['Cart'], request_body=CartUserSerializer)
    def create(self, request, *args, **kwargs):
        data = request.data
        user = data['user']
        user = AllCustomer.objects.get(id = int(user))
        try:
            cart = Cart.objects.get(user=user)
        except:
            cart = None
        if cart != None:
            cart = cart
        else:
            cart = Cart.objects.create(user=user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    # @swagger_auto_schema(tags=['Cart'])
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    
    # @swagger_auto_schema(tags=['Cart'])
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # @swagger_auto_schema(tags=['Cart'])
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)