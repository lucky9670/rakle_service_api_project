from django_filters import rest_framework as filters
from admin_api.models import MainService
from admin_api.serialization.main_service_serializer import MainServiceSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from lib.pagination import CustomPageNumberPagination
from rest_framework.parsers import MultiPartParser

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass



class MainServiceFilterClass(filters.FilterSet):
    main_service = NumberInFilter(field_name='id', lookup_expr='in', required=False,distinct=True)
    maincat_id = NumberInFilter(field_name='main_cat_name', lookup_expr='in', required=False,distinct=True)
    maincat_id = NumberInFilter(field_name='cat_name', lookup_expr='in', required=False,distinct=True)
    mserv_name =filters.CharFilter(method='filter_mser_name',required=False),
    mserv_status=filters.BooleanFilter(method='filter_mser_status',required=False),

    class Meta:
        model = MainService
        fields = ["id", 'main_cat_name', 'cat_name', 'main_service_name', 'status']

  
    # def filter_main_cat_id(self,querset,name,value):
    #     querset = querset.filter(maincat_id__id=value)   
    #     return querset

    def filter_mser_name(self,querset,name,value):
        querset = querset.filter(mserv_name__main_service_name=value)   
        return querset

    def filter_mser_status(self,querset,name,value):
        querset = querset.filter(mserv_status__status=value)   
        return querset



@swagger_auto_schema(tags=['Main Service Updated'])
class MainServiceView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = MainServiceSerializer
    filter_class = MainServiceFilterClass
    filterset_fields = ['id', 'main_cat_name', 'cat_name', 'main_service_name', 'status']
    pagination_class = CustomPageNumberPagination
    
    @swagger_auto_schema(tags=['Category Updated'])
    def get_queryset(self):
        return MainService.objects.all()


    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer =MainCategorySerializer(instance,context={'request':request})
    #     return Response(serializer.data)



    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.soft_delete()
    #     return JsonResponse({"status":True,"result":self.get_serializer(instance).data})
    