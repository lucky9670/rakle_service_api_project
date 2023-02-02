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


class CityView(GenericAPIView):
    serializer_class = CitySerializer

    @swagger_auto_schema(tags=['City'])
    def get(self,request):
        serializer_class=CitySerializer(data=request.data)
        try:
            obj=City.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Main_Cat':CitySerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['City'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "City": CitySerializer(city, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['City'],request_body=Update_City_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=CitySerializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=City.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)

            try:
                updatedata=City.objects.get(id=id)
                proj_check=City.objects.filter(city_name=info['city_name']).exclude(id=id).count()

                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                updatedata.city_name=info['city_name']
                updatedata.city_state=info.get('city_state')
                updatedata.city_countory=info.get('city_countory')
                updatedata.transdate=info.get('transdate')
                updatedata.status=info.get('status')

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  CitySerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_City(APIView):
    @swagger_auto_schema(tags=['City'],)
    def delete(self,request,city_id):
        try:
            project_obj=City.objects.get(id=city_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)



class CustomerView(GenericAPIView):
    serializer_class = CustomerSerializer

    @swagger_auto_schema(tags=['Customer'])
    def get(self,request):
        serializer_class=CustomerSerializer(data=request.data)
        try:
            obj=Customer.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Main_Cat':CustomerSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Customer'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "City": CustomerSerializer(city, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['Customer'],request_body=Update_Customer_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=CustomerSerializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=Customer.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)

            try:
                updatedata=Customer.objects.get(id=id)
                proj_check=Customer.objects.filter(customer_name=info['customer_name']).exclude(id=id).count()

                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                updatedata.customer_name=info['customer_name']
                updatedata.customer_gender=info.get('customer_gender')
                updatedata.customer_email=info.get('customer_email')
                updatedata.customer_phone=info.get('customer_phone')
                updatedata.customer_street=info.get('customer_street')
                updatedata.city=info.get('city')
                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  CustomerSerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_Customer(APIView):
    @swagger_auto_schema(tags=['Customer'],)
    def delete(self,request,c_id):
        try:
            project_obj=Customer.objects.get(id=c_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)



class VideoConsultationView(GenericAPIView):

    serializer_class = VideoConsultationSerializer

    @swagger_auto_schema(tags=['Video Consultation'])
    def get(self,request):
        serializer_class=VideoConsultationSerializer(data=request.data)
        try:
            obj=VideoConsultation.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','slider':VideoConsultationSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Video Consultation'])
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = VideoConsultationSerializer(data=request.data)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "Slider": VideoConsultationSerializer(plan, context=self.get_serializer_context()).data,
        })


class BookServiceView(GenericAPIView):
    serializer_class = BookServiceSerializer

    @swagger_auto_schema(tags=['Book Service'])
    def get(self,request):
        serializer_class=BookServiceSerializer(data=request.data)
        try:
            obj=BookService.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':BookServiceSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Book Service'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": BookServiceSerializer(city, context=self.get_serializer_context()).data,
        })

    # @swagger_auto_schema(tags=['Book Service'],request_body=Update_BookService_Serializer)
    # def put(self,request,*args,**kwargs):
    #     # import pdb;pdb.set_trace()
    #     info=request.data
    #     update_serializer=CustomerSerializer(data=request.data)

    #     if update_serializer.is_valid():
    #         id=info['id']
    #         check=BookService.objects.filter(id=id).count()
    #         # try:
    #         #     project_check=UserProfile.objects.get(id=info['user_profile'])
    #         # except Exception as e:
    #         #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
    #         if check==0:
    #             return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)

    #         try:
    #             updatedata=Customer.objects.get(id=id)
    #             proj_check=Customer.objects.filter(customer_name=info['customer_name']).exclude(id=id).count()

    #             if proj_check !=0:
    #                 return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
    #             updatedata.customer_name=info['customer_name']
    #             updatedata.customer_gender=info.get('customer_gender')
    #             updatedata.customer_email=info.get('customer_email')
    #             updatedata.customer_phone=info.get('customer_phone')
    #             updatedata.customer_street=info.get('customer_street')
    #             updatedata.city=info.get('city')
    #             updatedata.save()
    #         except Exception as e:
    #             return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
    #         return JsonResponse({"result": "true", "response": "project has been updated successfully.",
    #                             "data":  CustomerSerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
    #     else:
    #         return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_BookService(APIView):
    @swagger_auto_schema(tags=['Book Service'],)
    def delete(self,request,bs_id):
        try:
            project_obj=BookService.objects.get(id=bs_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)



class PartnerView(GenericAPIView):
    serializer_class = PartnerSerializer

    @swagger_auto_schema(tags=['Partner'])
    def get(self,request):
        serializer_class=PartnerSerializer(data=request.data)
        try:
            obj=Partner.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_Partner(APIView):
    @swagger_auto_schema(tags=['Partner'],)
    def delete(self,request,par_id):
        try:
            project_obj=Partner.objects.get(id=par_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)

class PartnerDocumentView(GenericAPIView):
    serializer_class = PartnerDocumentSerializer

    @swagger_auto_schema(tags=['Partner Docs'])
    def get(self,request):
        serializer_class=PartnerDocumentSerializer(data=request.data)
        try:
            obj=PartnerDocument.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerDocumentSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Docs'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerDocumentSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerDocument(APIView):
    @swagger_auto_schema(tags=['Partner Docs'],)
    def delete(self,request,pd_id):
        try:
            project_obj=PartnerDocument.objects.get(id=pd_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)


class PartnerProffetionalDetailView(GenericAPIView):
    serializer_class = PartnerProffetionalDetailSerializer

    @swagger_auto_schema(tags=['Partner Portfetion Detail'])
    def get(self,request):
        serializer_class=PartnerProffetionalDetailSerializer(data=request.data)
        try:
            obj=PartnerProffetionalDetail.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerProffetionalDetailSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Portfetion Detail'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerProffetionalDetailSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerProffetionalDetail(APIView):
    @swagger_auto_schema(tags=['Partner Portfetion Detail'],)
    def delete(self,request,ppd_id):
        try:
            project_obj=PartnerProffetionalDetail.objects.get(id=ppd_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)



class PartnerWorkBookView(GenericAPIView):
    serializer_class = PartnerWorkBookSerializer

    @swagger_auto_schema(tags=['Partner Work Book'])
    def get(self,request):
        serializer_class=PartnerWorkBookSerializer(data=request.data)
        try:
            obj=PartnerWorkBook.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerWorkBookSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Work Book'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerWorkBookSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerWorkBook(APIView):
    @swagger_auto_schema(tags=['Partner Work Book'],)
    def delete(self,request,pwb_id):
        try:
            project_obj=PartnerWorkBook.objects.get(id=pwb_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)




class PartnerAwardAndPhoteView(GenericAPIView):
    serializer_class = PartnerAwardAndPhoteSerializer

    @swagger_auto_schema(tags=['Partner Award and Portfolio'])
    def get(self,request):
        serializer_class=PartnerAwardAndPhoteSerializer(data=request.data)
        try:
            obj=PartnerAwardAndPhote.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerAwardAndPhoteSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Award and Portfolio'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerAwardAndPhoteSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerAwardAndPhote(APIView):
    @swagger_auto_schema(tags=['Partner Award and Portfolio'],)
    def delete(self,request,pap_id):
        try:
            project_obj=PartnerAwardAndPhote.objects.get(id=pap_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)





class PartnerServiceLocationView(GenericAPIView):
    serializer_class = PartnerServiceLocationSerializer

    @swagger_auto_schema(tags=['Partner Service Location'])
    def get(self,request):
        serializer_class=PartnerServiceLocationSerializer(data=request.data)
        try:
            obj=PartnerServiceLocation.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerServiceLocationSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Service Location'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerServiceLocationSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerServiceLocationView(APIView):
    @swagger_auto_schema(tags=['Partner Service Location'],)
    def delete(self,request,psl_id):
        try:
            project_obj=PartnerServiceLocation.objects.get(id=psl_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)



class PartnerServiceRefrenceView(GenericAPIView):
    serializer_class = PartnerServiceRefrenceSerializer

    @swagger_auto_schema(tags=['Partner Service Refrence'])
    def get(self,request):
        serializer_class=PartnerServiceRefrenceSerializer(data=request.data)
        try:
            obj=PartnerServiceRefrence.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','book':PartnerServiceRefrenceSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Partner Service Refrence'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        return Response({
            "book": PartnerServiceRefrenceSerializer(city, context=self.get_serializer_context()).data,
        })

class Delete_PartnerServiceRefrence(APIView):
    @swagger_auto_schema(tags=['Partner Service Refrence'],)
    def delete(self,request,psr1_id):
        try:
            project_obj=PartnerServiceRefrence.objects.get(id=psr1_id).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)