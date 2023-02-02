from knox.models import AuthToken
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from admin_api.serialization.work_serializer import *
from django.conf import settings
from admin_api.models import *
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.utils import timezone
from admin_api.serialization.update_serializer import *
from rest_framework.parsers import MultiPartParser, FormParser

class OfferView(GenericAPIView):

    serializer_class = BestOfferGetSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(tags=['Best Offer'])
    def get(self,request):
        serializer_class=BestOfferGetSerializer(data=request.data)
        try:
            obj=BestOffer.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','offer':BestOfferGetSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Best Offer'])
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = BestOfferSerializer(data=request.data)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "offer": BestOfferGetSerializer(plan, context=self.get_serializer_context()).data,
        })


class UserReviewView(GenericAPIView):

    serializer_class = UserReviewSerializer

    @swagger_auto_schema(tags=['User Review'])
    def get(self,request):
        serializer_class=UserReviewSerializer(data=request.data)
        try:
            obj=UserReview.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Review':UserReviewSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['User Review'])
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = UserReviewSerializer(data=request.data)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "Review": UserReviewSerializer(plan, context=self.get_serializer_context()).data,
        })


class Delete_UserReview(APIView):
    @swagger_auto_schema(tags=['User Review'])
    def delete(self,request,ur_id):
        try:
            project_obj=UserReview.objects.get(id=ur_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'Review deleted successfully'},safe=False)




class AddToCartView(GenericAPIView):

    serializer_class = AddToCartSerializer

    @swagger_auto_schema(tags=['Add to Cart'])
    def get(self,request):
        serializer_class=AddToCartSerializer(data=request.data)
        try:
            obj=AddToCart.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Review':AddToCartSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Add to Cart'])
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = AddToCartSerializer(data=request.data)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "Review": AddToCartSerializer(plan, context=self.get_serializer_context()).data,
        })


class Delete_AddToCart(APIView):
    @swagger_auto_schema(tags=['Add to Cart'])
    def delete(self,request,ur_id):
        try:
            project_obj=AddToCart.objects.get(id=ur_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'Review deleted successfully'},safe=False)




