from rest_framework.viewsets import ViewSet
from app_login.serials.vender_serilizer import ProfileUpdateSerializer, ProfilePictureUpdateSerializer, BasicUpdateSerializer, BankUpdateSerializer, VenderSerializer
from drf_yasg.utils import swagger_auto_schema
from app_login.models import VenderProfile, UserSignupModel
from rest_framework.parsers import MultiPartParser
from django.http import JsonResponse
from rest_framework.response import Response

class BankUpdateView(ViewSet):
    serializer_class = ProfileUpdateSerializer

    @swagger_auto_schema(tags=["Profile Update"])
    def get_queryset(self):
        return VenderProfile.objects.all()
    
    @swagger_auto_schema(tags=["Profile Update"])
    def list(self,request):
        vender =VenderProfile.objects.all()
        serializer=VenderSerializer(vender, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=["Profile Update"])
    def retrieve(self, request, pk=None):
        user = UserSignupModel.objects.get(id=pk)
        queryset = VenderProfile.objects.get(user=user)
        serializer=VenderSerializer(queryset)
        return Response(serializer.data)

    @swagger_auto_schema(tags=["Profile Update"], request_body=BankUpdateSerializer)
    def create(self, request, *args, **kwargs):
        data = request.data
        user = data['user']
        aadhar_card = data['aadhar_card']
        pan_card = data['pan_card']
        account_number = data['account_number']
        ifsc_code = data['ifsc_code']
        account_holder = data['account_holder']
        bank_name = data['bank_name']
        branch = data['branch']
        try:
            user_data = UserSignupModel.objects.get(id=user)
            profile = VenderProfile.objects.get(user=user_data)
        except:
            profile = None
        if profile != None:
            profile.aadhar_card = aadhar_card
            profile.pan_card = pan_card
            profile.account_number = account_number
            profile.ifsc_code = ifsc_code
            profile.account_holder = account_holder
            profile.bank_name = bank_name
            profile.branch = branch
            profile.save()
        else:
            data = VenderProfile.objects.create(user=user, aadhar_card=aadhar_card, pan_card=pan_card, account_number=account_number,ifsc_code=ifsc_code, account_holder=account_holder, bank_name=bank_name, branch=branch)

        return JsonResponse({"result":"Success", "response":"Profile Updated"})

class GeneralUpdateView(ViewSet):
    serializer_class = ProfileUpdateSerializer

    @swagger_auto_schema(tags=["Profile Update"])
    def get_queryset(self):
        return VenderProfile.objects.all()

    @swagger_auto_schema(tags=["Profile Update"], request_body=BasicUpdateSerializer)
    def create(self, request, *args, **kwargs):
        data = request.data
        user = data['user']
        address = data['address']
        latitude = data['latitude']
        longitude = data['longitude']
        qualification = data['qualification']
        age = data['age']
        gender = data['gender']
        notification_id = data['notification_id']
        email = data.get('email')
        amount = data.get('amount')
        no_of_vender = data.get('no_of_vender')
        try:
            profile = VenderProfile.objects.get(user=user)
        except:
            profile = None
        if profile != None:
            profile.address = address
            profile.latitude = latitude
            profile.longitude = longitude
            profile.qualification = qualification
            profile.age = age
            profile.gender = gender
            profile.notification_id = notification_id
            profile.email = email
            profile.amount = amount
            profile.no_of_vender = no_of_vender
            profile.save()
        else:
            data = VenderProfile.objects.create(user=user, address=address, latitude=latitude, longitude=longitude,qualification=qualification, age=age, gender=gender, notification_id=notification_id, email=email, no_of_vender=no_of_vender, amount=amount)

        return JsonResponse({"result":"Success", "response":"Profile Updated"})

class ImageUpdateView(ViewSet):
    serializer_class = ProfileUpdateSerializer
    parser_classes = (MultiPartParser, )

    @swagger_auto_schema(tags=["Profile Update"], request_body=ProfilePictureUpdateSerializer)
    def create(self, request, *args, **kwargs):
        data = request.data
        user = data['user']
        image = data['image']
        try:
            profile = VenderProfile.objects.get(user=user)
        except:
            profile = None
        if profile != None:
            profile.image = image
            profile.save()
        else:
            data = VenderProfile.objects.create(user=user, image=image)
        return JsonResponse({"result":"Success", "response":"Profile Updated"})