from rest_framework import serializers
from admin_api.models import MainCategory

class MainCategorySerializer(serializers.ModelSerializer):
    # main_cat_name=serializers.CharField(required=False)
    # status=serializers.BooleanField(required=False)

    class Meta:
        model = MainCategory
        fields=["id",'main_cat_name','status',"main_cat_image","created_at","modified_at","transfer_date",'ref']
