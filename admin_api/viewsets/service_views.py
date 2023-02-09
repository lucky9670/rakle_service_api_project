from django_filters import rest_framework as filters
from admin_api.models import Service, AddToCart
from admin_api.serialization.service_serializer import ServiceSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
from rest_framework.parsers import MultiPartParser
from app_login.models import AllCustomer
from django.http import JsonResponse
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        data = []
        try:
            print("")
            print("===================")
            user = int(self.request.query_params["user"])
        except:
            user = None
        if user is not None:
            user = AllCustomer.objects.get(id=user)
            for item in queryset:
                service = Service.objects.get(id = item.id)
                try:
                    addtocart = AddToCart.objects.get(user=user, service=service)
                    service_quantity = addtocart.service_quantity
                except:
                    service_quantity = 0
                result = {
                    'id':service.id,
                    'main_cat_name':service.main_cat_name.id,
                    'cat_name':service.cat_name.id,
                    'main_service_name':service.main_service_name.id,
                    'service_name':service.service_name,
                    'status':service.status,
                    'service_image':service.service_image.url,
                    'service_charge':service.service_charge,
                    'service_time':service.service_time,
                    'discount':service.discount,
                    'service_quantity':service_quantity,
                }
                data.append(result)
        print(data)
        return JsonResponse({'status': 'Success', 'message': 'You have signin successfully!', 'data': data}, safe=False)
        
        # page = self.paginate_queryset(data)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(data, many=True)
        # return Response(serializer.data)
