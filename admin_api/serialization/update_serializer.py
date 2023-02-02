from rest_framework import serializers
from admin_api.models import *

class Update_City_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=City
        fields=('id','city_name','city_state','city_countory',"transdate", "status")

class Update_Customer_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=Customer
        fields=('id','customer_name','customer_gender','customer_email',"customer_phone", "customer_street","city")

class Update_BookService_Serializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    
    class Meta:
        model=BookService
        fields=('id','bookser_date','bookser_time','bookser_remark',"payment_method", "transdate","customer_id",'service')
