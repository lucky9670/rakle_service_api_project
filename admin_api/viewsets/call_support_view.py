
from admin_api.serialization.call_support_serial import VendorCallSupportSerial
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
from admin_api.models import VendorCallSupport
from django_filters import rest_framework as filters


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class ServiceFilterClass(filters.FilterSet):
    service = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)
    vendor_id = NumberInFilter(field_name='vendor', lookup_expr='in', required=False,distinct=True)

    class Meta:
        model = VendorCallSupport
        fields = ["id", 'vendor']


@swagger_auto_schema(tags=['Call Support API'])
class VenderCallSupportView( viewsets.ModelViewSet):
    serializer_class = VendorCallSupportSerial
    filter_class =  ServiceFilterClass
    filterset_fields = ['id', 'vendor']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Call Support API'])
    def get_queryset(self):
        return VendorCallSupport.objects.all()
