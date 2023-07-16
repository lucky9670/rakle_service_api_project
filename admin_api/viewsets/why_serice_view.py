from django_filters import rest_framework as filters
from admin_api.models import WhyService
from admin_api.serialization.why_service_serializer import WhyServiceSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
from rest_framework.parsers import MultiPartParser
class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass



class WhyServiceFilterClass(filters.FilterSet):
    service = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)

    class Meta:
        model = WhyService
        fields = ["id", 'service']

    def filter_ser_name(self,querset,name,value):
        querset = querset.filter(service__service=value)   
        return querset


@swagger_auto_schema(tags=['Why Service'])
class WhyServiceView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = WhyServiceSerializer
    filter_class =  WhyServiceFilterClass
    filterset_fields = ['id', 'service']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Why Service'])
    def get_queryset(self):
        return WhyService.objects.all()
