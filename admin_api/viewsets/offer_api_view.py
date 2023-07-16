from django_filters import rest_framework as filters
from admin_api.models import BestOffer
from admin_api.serialization.offer_serializer import BestOfferGetSerializer
from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
import datetime
from django.http import JsonResponse,Http404
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass



class OfferFilterClass(filters.FilterSet):
    offer_id = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)
    ofeer_name = filters.CharFilter(method='filter_name_name',required=False),
    offer_service = NumberInFilter(method='filter_offer_service',required=False),

    class Meta:
        model = BestOffer
        fields = ["id", 'name', 'service']

    def filter_name_name(self,querset,name,value):
        querset = querset.filter(main_cat_name__main_cat_name=value)   
        return querset

    def filter_offer_service(self,querset,name,value):
        querset = querset.filter(main_cat_status__status=value)   
        return querset



@swagger_auto_schema(tags=['Best Offer APIs'])
class BestOfferView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = BestOfferGetSerializer
    filter_class = OfferFilterClass
    filterset_fields = ["id", 'name', 'service']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Best Offer APIs'])
    def get_queryset(self):
        return BestOffer.objects.all()
