from django_filters import rest_framework as filters
from admin_api.models import Service
from admin_api.serialization.service_serializer import ServiceSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
from rest_framework.parsers import MultiPartParser

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass



class ServiceFilterClass(filters.FilterSet):
    service = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)
    maincat_id = NumberInFilter(field_name='main_cat_name', lookup_expr='in', required=False,distinct=True)
    cat_id = NumberInFilter(field_name='cat_name', lookup_expr='in', required=False,distinct=True)
    mserv_id = NumberInFilter(field_name='main_service_name', lookup_expr='in', required=False,distinct=True)
    service_name=filters.CharFilter(method='filter_ser_name',required=False),
    service_status=filters.BooleanFilter(method='filter_ser_status',required=False),
    service_prices=filters.BooleanFilter(method='filter_ser_price',required=False),

    class Meta:
        model = Service
        fields = ["id", 'main_cat_name', 'cat_name', 'main_service_name', 'service_name', 'status', 'service_charge']

    def filter_ser_name(self,querset,name,value):
        querset = querset.filter(serv_name__service_name=value)   
        return querset

    def filter_ser_status(self,querset,name,value):
        querset = querset.filter(serv_status__status=value)   
        return querset

    def filter_ser_price(self,querset,name,value):
        querset = querset.filter(service_prices__service_charge=value)   
        return querset



@swagger_auto_schema(tags=['Main Service Updated'])
class ServiceView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = ServiceSerializer
    filter_class =  ServiceFilterClass
    filterset_fields = ['id', 'main_cat_name', 'cat_name', 'main_service_name', 'service_name', 'status', 'service_charge']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Category Updated'])
    def get_queryset(self):
        return Service.objects.all()
        