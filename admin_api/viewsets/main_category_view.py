from django_filters import rest_framework as filters
from admin_api.models import MainCategory
from admin_api.serialization.main_category_serializer import MainCategorySerializer
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



class MainCatFilterClass(filters.FilterSet):
    maincat_id = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)
    main_cat_name=filters.CharFilter(method='filter_maincat_name',required=False),
    main_cat_status=filters.BooleanFilter(method='filter_maincat_status',required=False),

    class Meta:
        model = MainCategory
        fields = ["id", 'main_cat_name', 'status']

  
    # def filter_main_cat_id(self,querset,name,value):
    #     querset = querset.filter(maincat_id__id=value)   
    #     return querset

    def filter_maincat_name(self,querset,name,value):
        querset = querset.filter(main_cat_name__main_cat_name=value)   
        return querset

    def filter_maincat_status(self,querset,name,value):
        querset = querset.filter(main_cat_status__status=value)   
        return querset



@swagger_auto_schema(tags=['Main Category Updated'])
class MainCategoryView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = MainCategorySerializer
    filter_class = MainCatFilterClass
    filterset_fields = ["id", 'main_cat_name', 'status']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Main Category Updated'])
    def get_queryset(self):
        return MainCategory.objects.all()


    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer =MainCategorySerializer(instance,context={'request':request})
    #     return Response(serializer.data)



    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.soft_delete()
    #     return JsonResponse({"status":True,"result":self.get_serializer(instance).data})
    