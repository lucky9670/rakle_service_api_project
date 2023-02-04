from rest_framework.response import Response
from admin_api.models import AddToCart
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from admin_api.serialization.add_to_cart_serializer import AddToCartSerializer
from rest_framework.parsers import MultiPartParser


class AddToCartView(ModelViewSet):
    serializer_class = AddToCartSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(tags=["Add To Cart"])
    def get_queryset(self):
        return AddToCart.objects.all()
    