from admin_api.models import AboutService
from admin_api.serialization.service_about_serializer import AboutServiceSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser


@swagger_auto_schema(tags=['Main Service Updated'])
class AboutServiceView( viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = AboutServiceSerializer
    
    @swagger_auto_schema(tags=['Category Updated'])
    def get_queryset(self):
        return AboutService.objects.all()
        