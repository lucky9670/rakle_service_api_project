from knox.models import AuthToken
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from .services_serializer import *
from django.conf import settings
from .models import *
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser


class MainCategoryView(GenericAPIView):
    serializer_class = MainCategorySerializer

    @swagger_auto_schema(tags=['Main Category'])
    def get(self,request):
        serializer_class=MainCategorySerializer(data=request.data)
        try:
            obj=MainCategory.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Main_Cat':MainCategorySerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Main Category'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        return Response({
            "plan": MainCategorySerializer(plan, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['Main Category'],request_body=Update_MainCat_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=Update_MainCat_Serializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=MainCategory.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)

            try:
                updatedata=MainCategory.objects.get(id=id)

                

                proj_check=MainCategory.objects.filter(main_cat_name=info['main_cat_name']).exclude(id=id).count()

                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                updatedata.main_cat_name=info['main_cat_name']
                updatedata.status=info.get('status')
                updatedata.main_cat_image=info.get('main_cat_image')
                updatedata.modified_at=timezone.now()

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  MainCategorySerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_MainCat(APIView):
    @swagger_auto_schema(tags=['Main Category'],)
    def delete(self,request,mainid):
        try:
            project_obj=MainCategory.objects.get(id=mainid).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)

    
class CategoryView(GenericAPIView):

    serializer_class = CategorySerializer

    @swagger_auto_schema(tags=['Category'])
    def get(self,request):
        serializer_class=CategorySerializer(data=request.data)
        try:
            obj=Category.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Sub_Cat':CategorySerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Category'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        return Response({
            "Cat": CategorySerializer(plan, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['Category'],request_body=Update_Cat_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=Update_Cat_Serializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=Category.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)
            # import pdb;pdb.set_trace()
            try:
                updatedata=Category.objects.get(id=id)
                proj_check=Category.objects.filter(cat_name=info['cat_name']).exclude(id=id).count()
                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                mincat=MainCategory.objects.get(id=info['main_cat_name'])
                updatedata.cat_name=info.get('cat_name')
                updatedata.status=info.get('status')
                updatedata.cat_image=info.get('cat_image')
                updatedata.main_cat_name=mincat
                updatedata.modified_at=timezone.now()

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  CategorySerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)

class Delete_Cat(APIView):
    @swagger_auto_schema(tags=['Category'],)
    def delete(self,request,catid):
        try:
            project_obj=Category.objects.get(id=catid).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)

    

    
class MainServiceView(GenericAPIView):
    serializer_class = MainServiceSerializer

    @swagger_auto_schema(tags=['Main Service'])
    def get(self,request):
        serializer_class=MainServiceSerializer(data=request.data)
        try:
            obj=MainService.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','main services':MainServiceSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Main Service'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        return Response({
            "Main Service": MainServiceSerializer(plan, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['Main Service'],request_body=Update_MainSer_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=Update_MainSer_Serializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=Category.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)
            # import pdb;pdb.set_trace()
            try:
                updatedata=MainService.objects.get(id=id)
                proj_check=MainService.objects.filter(main_service_name=info['main_service_name']).exclude(id=id).count()
                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                mincat=MainCategory.objects.get(id=info['main_cat_name'])
                cat=Category.objects.get(id=info['cat_name'])
                updatedata.main_service_name=info.get('main_service_name')
                updatedata.status=info.get('status')
                updatedata.cat_image=info.get('cat_image')
                updatedata.main_cat_name=mincat
                updatedata.cat_name=cat
                updatedata.modified_at=timezone.now()

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  MainServiceSerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_MainService(APIView):
    @swagger_auto_schema(tags=['Main Service'])
    def delete(self,request,mserid):
        try:
            project_obj=MainService.objects.get(id=mserid).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)

    
class ServiceView(GenericAPIView):

    serializer_class = ServiceSerializer

    @swagger_auto_schema(tags=['Service'])
    def get(self,request):
        serializer_class=ServiceSerializer(data=request.data)
        try:
            obj=Service.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','services':ServiceSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Service'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        return Response({
            "Main Service": ServiceSerializer(plan, context=self.get_serializer_context()).data,
        })

    @swagger_auto_schema(tags=['Service'],request_body=Update_Service_Serializer)
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=Update_Service_Serializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=Service.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)
            # import pdb;pdb.set_trace()
            try:
                updatedata=Service.objects.get(id=id)
                proj_check=Service.objects.filter(service_name=info['service_name']).exclude(id=id).count()
                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                mincat=MainCategory.objects.get(id=info['main_cat_name'])
                cat=Category.objects.get(id=info['cat_name'])
                mser=MainService.objects.get(id=info['main_service_name'])
                updatedata.service_name=info.get('service_name')
                updatedata.status=info.get('status')
                updatedata.service_image=info.get('service_image')
                updatedata.service_charge=info.get('service_charge')
                updatedata.service_time=info.get('service_time')
                updatedata.discount=info.get('discount')
                updatedata.main_cat_name=mincat
                updatedata.main_service_name=mser
                updatedata.cat_name=cat
                updatedata.modified_at=timezone.now()

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  ServiceSerializer(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_Service(APIView):
    @swagger_auto_schema(tags=['Service'])
    def delete(self,request,serid):
        try:
            project_obj=Service.objects.get(id=serid).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)
    @swagger_auto_schema(tags=['Service'])
    def get(self,request,serid):
        try:
            project_obj=Service.objects.get(id=serid)
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        return Response({
            "Service": ServiceSerializer(project_obj).data,
        })
        # return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)             

class AboutSerGet(ViewSet):
    @swagger_auto_schema(tags=['About Service'],)
    @action(detail=False, methods=['get'])
    def get_about_ser_by_id(self,request,ser_id):
        
        #import pdb;pdb.set_trace()
        service1 = Service.objects.get(id=ser_id)
        obj=AboutService.objects.filter(service_name=service1)[::-1]
        if not obj: 
            return JsonResponse({'result':"false",'response':"no data present"},safe=False)
        return JsonResponse({'result':"true",'about_service':AboutServiceSerializer(obj,many=True).data},safe=False)

class AboutServiceView(GenericAPIView):
    serializer_class = AboutServiceSerializerother
    @swagger_auto_schema(tags=['About Service'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  AboutServiceSerializerother(plan, context=self.get_serializer_context()).data}, safe=False)
        # return Response({
        #     "Main Service": AboutServiceSerializerother(plan, context=self.get_serializer_context()).data,
        # })

    @swagger_auto_schema(tags=['About Service'],request_body=Update_ServiceAbout_Serializer)
    @action(detail=False, methods=['put'])
    def put(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        info=request.data
        update_serializer=Update_ServiceAbout_Serializer(data=request.data)

        if update_serializer.is_valid():
            id=info['id']
            check=AboutService.objects.filter(id=id).count()
            # try:
            #     project_check=UserProfile.objects.get(id=info['user_profile'])
            # except Exception as e:
            #     return JsonResponse({'result':'false','response':'Please enter valid project id.'},safe=False)
            if check==0:
                return JsonResponse({'result':'false','response':'Data not present please enter valid data.'},safe=False)
            # import pdb;pdb.set_trace()
            try:
                updatedata=AboutService.objects.get(id=id)
                proj_check=AboutService.objects.filter(name=info['name']).exclude(id=id).count()
                if proj_check !=0:
                    return JsonResponse({'result':'false','response':'project name already exist'},safe=False)
                
                # mincat=MainCategory.objects.get(id=info['main_cat_name'])
                # cat=Category.objects.get(id=info['cat_name'])
                # mser=MainService.objects.get(id=info['main_service_name'])
                ser=Service.objects.get(id=info['service_name'])
                updatedata.title=info.get('title')
                # updatedata.status=info.get('status')
                updatedata.image=info.get('image')
                updatedata.video=info.get('video')
                # updatedata.service_time=info.get('service_time')
                updatedata.discription=info.get('discription')
                updatedata.notes=info.get('notes')
                # updatedata.main_cat_name=mincat
                # updatedata.main_service_name=mser
                # updatedata.cat_name=cat
                updatedata.service_name=ser
                updatedata.modified_at=timezone.now()

                updatedata.save()
            except Exception as e:
                return JsonResponse({"result": "false", "response": "something went wrong."}, safe=False)
            return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  AboutServiceSerializerother(updatedata, context=self.get_serializer_context()).data}, safe=False)
        else:
            return JsonResponse({"result": "false", "response": "Please enter valid details."}, safe=False)


class Delete_ServiceAbout(APIView):
    @swagger_auto_schema(tags=['About Service'])
    def delete(self,request,aserid):
        try:
            project_obj=AboutService.objects.get(id=aserid).delete()
        except:
            return JsonResponse({'result':'false','response':'please insert valid test id'})
        
        return JsonResponse({'result':"true",'response':'test deleted successfully'},safe=False)





class SliderView(GenericAPIView):

    serializer_class = SliderGetSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(tags=['Slider'])
    def get(self,request):
        serializer_class=SliderGetSerializer(data=request.data)
        try:
            obj=Slider.objects.all()
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','slider':SliderGetSerializer(obj,many=True).data},safe=False)

    @swagger_auto_schema(tags=['Slider'])
    def post(self, request, *args, **kwargs):
        try:
            file_serializer = SliderSerializer(data=request.data)
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response({
            "Slider": SliderGetSerializer(plan, context=self.get_serializer_context()).data,
        })


class CategoryByMaincat(APIView):

    serializer_class = CategorySerializer

    @swagger_auto_schema(tags=['Filter API'])
    def get(self,request,mainrid):
        serializer_class=CategorySerializer(data=request.data)
        try:
            maincat = MainCategory.objects.get(id= mainrid)
            user_data=request.user
            obj=Category.objects.filter(main_cat_name=maincat)
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Sub_Cat':CategorySerializer(obj,many=True).data},safe=False)

class MainserByCat(APIView):

    serializer_class = MainServiceSerializer

    @swagger_auto_schema(tags=['Filter API'])
    def get(self,request,cat1id):
        serializer_class=MainServiceSerializer(data=request.data)
        try:
            cat = Category.objects.get(id= cat1id)
            user_data=request.user
            obj=MainService.objects.filter(cat_name=cat)
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Sub_Cat':MainServiceSerializer(obj,many=True).data},safe=False)

class ServByMainser(APIView):

    serializer_class = ServiceSerializer

    @swagger_auto_schema(tags=['Filter API'])
    def get(self,request,mainserid):
        serializer_class=ServiceSerializer(data=request.data)
        try:
            mainser = MainService.objects.get(id= mainserid)
            user_data=request.user
            obj=Service.objects.filter(main_service_name=mainser)
        except:
            return JsonResponse({'result':'false','response':'Something went wrong, Please check.'})
        return JsonResponse({'result':'true','Sub_Cat':ServiceSerializer(obj,many=True).data},safe=False)


class ServicePackage(ViewSet):
    @swagger_auto_schema(tags=['Service Package'],)
    @action(detail=False, methods=['get'])
    def get_package_by_ser_id(self,request,ser_id):
        
        #import pdb;pdb.set_trace()
        service1 = Service.objects.get(id=ser_id)
        obj=Package.objects.filter(service=service1)[::-1]
        if not obj: 
            return JsonResponse({'result':"false",'response':"no data present"},safe=False)
        return JsonResponse({'result':"true",'about_service':PackageSerializer(obj,many=True).data},safe=False)

class ServicePackageView(GenericAPIView):
    serializer_class = PackageSerializer
    @swagger_auto_schema(tags=['Service Package'])
    # @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return JsonResponse({"result": "true", "response": "project has been updated successfully.",
                                "data":  PackageSerializer(plan, context=self.get_serializer_context()).data}, safe=False)
        

class ServiceFAQGet(ViewSet):
    @swagger_auto_schema(tags=['Service FAQ'],)
    @action(detail=False, methods=['get'])
    def get_faq_by_ser_id(self,request,ser_id):
        
        #import pdb;pdb.set_trace()
        service1 = Service.objects.get(id=ser_id)
        obj=ServiceFAQ.objects.filter(service=service1)[::-1]
        if not obj: 
            return JsonResponse({'result':"false",'response':"no data present"},safe=False)
        return JsonResponse({'result':"true",'about_service':ServiceFAQSerializer(obj,many=True).data},safe=False)

class ServiceFAQView(GenericAPIView):
    serializer_class = ServiceFAQSerializer
    @swagger_auto_schema(tags=['Service FAQ'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return JsonResponse({"result": "true", "response": "Package has been added successfully.",
                                "data":  ServiceFAQSerializer(plan, context=self.get_serializer_context()).data}, safe=False)



class HomeCleaning(GenericAPIView):
    serializer_class = ServiceFAQSerializer
    @swagger_auto_schema(tags=['Service FAQ'])
    @action(detail=False, methods=['post'])
    def post(self, request, *args, **kwargs):

        try:
            check_data = request.data
        except Exception as e:
            return JsonResponse({'result': 'fail', 'response': 'Something went wrong, Please check.'}, safe=False)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return JsonResponse({"result": "true", "response": "Package has been added successfully.",
                                "data":  ServiceFAQSerializer(plan, context=self.get_serializer_context()).data}, safe=False)



