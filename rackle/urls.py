from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework.routers import DefaultRouter
from admin_api.viewsets.city_views import Delete_City
# from app_login.user_api import LoginView, SignupView
from admin_api.service_views import *
from admin_api.viewsets.city_views import *
from admin_api.viewsets.newviews import *
from admin_api.viewsets.payment_gateway import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="News Engine",
        default_version='v1',
        description="Welcome to the world of News",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# userapi = DefaultRouter()
# userapi.register(r'login', LoginView, basename="login")
# userapi.register(r'signup', SignupView, basename="signup")


urlpatterns = [
    path('api/v2/main_cat', MainCategoryView.as_view(), name='main-category-get'),
    path('api/v2/main_cat', MainCategoryView.as_view(), name='main-category-post'),
    path('api/v2/main_cat', MainCategoryView.as_view(), name='main-category-put'),
    path('api/v2/main_cat/<int:mainid>',Delete_MainCat.as_view(),name='delete_created_maincat'),

    path('api/v2/cat', CategoryView.as_view(), name='category-get'),
    path('api/v2/cat', CategoryView.as_view(), name='category-post'),
    path('api/v2/cat', CategoryView.as_view(), name='category-put'),
    path('api/v2/cat/<int:catid>',Delete_Cat.as_view(),name='delete_created_cat'),

    path('api/v2/cat_by_maincat/<int:mainrid>', CategoryByMaincat.as_view(), name='category-filter-by-maincat'),
    path('api/v2/mainser_by_cat/<int:cat1id>', MainserByCat.as_view(), name='mainser-filter-by-cat'),
    path('api/v2/ser_by_mainser/<int:mainserid>', ServByMainser.as_view(), name='ser-filter-by-mainser'),

    path('api/v2/main_service', MainServiceView.as_view(), name='mainservice-get'),
    path('api/v2/main_service', MainServiceView.as_view(), name='mainservice-post'),
    path('api/v2/main_service', MainServiceView.as_view(), name='mainservice-put'),
    path('api/v2/main_service/<int:mserid>',Delete_MainService.as_view(),name='delete_mainservice_cat'),

    path('api/v2/service', ServiceView.as_view(), name='service-get'),
    path('api/v2/service', ServiceView.as_view(), name='service-post'),
    path('api/v2/service', ServiceView.as_view(), name='service-put'),
    path('api/v2/service/<int:serid>',Delete_Service.as_view(),name='delete_service_cat'),
    path('api/v2/service/<int:serid>',Delete_Service.as_view(),name='service_cat'),

    path('api/v2/about_service/<int:ser_id>',AboutSerGet.as_view({'get':'get_about_ser_by_id'}),name='about_service_get'),
    # path('api/v2/about_service', AboutServiceView.as_view(), name='about-service-get'),
    path('api/v2/about_service', AboutServiceView.as_view(),name='about_service_post'),
    path('api/v2/about_service', AboutServiceView.as_view(), name='about_service_put'),
    path('api/v2/about_service/<int:aserid>',Delete_ServiceAbout.as_view(),name='delete_about_service_cat'),

    path('api/v2/service_package/<int:ser_id>',ServicePackage.as_view({'get':'get_package_by_ser_id'}),name='service_package_get'),
    path('api/v2/service_package', ServicePackageView.as_view(),name='service_package_post'),

    path('api/v2/service_faq/<int:ser_id>',ServiceFAQGet.as_view({'get':'get_faq_by_ser_id'}),name='service_faq_get'),
    path('api/v2/service_faq', ServiceFAQView.as_view(),name='service_faq_post'),

    path('api/v2/slider', SliderView.as_view(), name='slider-get'),
    path('api/v2/slider', SliderView.as_view(), name='slider-post'),

    path('api/v2/video_consultation', VideoConsultationView.as_view(), name='video-consult-get'),
    path('api/v2/video_consultation', VideoConsultationView.as_view(), name='video-consult-post'),
    
    # City
    path('api/v2/city', CityView.as_view(), name='city-get'),
    path('api/v2/city', CityView.as_view(), name='city-post'),
    path('api/v2/city', CityView.as_view(), name='city-put'),
    path('api/v2/city/<int:city_id>',Delete_City.as_view(),name='delete_city'),

    # City
    # path('api/v2/customer', CustomerView.as_view(), name='customer-get'),
    # path('api/v2/customer', CustomerView.as_view(), name='customer-post'),
    # path('api/v2/customer', CustomerView.as_view(), name='customer-put'),
    # path('api/v2/customer/<int:c_id>',Delete_Customer.as_view(),name='delete_customer'),

    # bast offer
    path('api/v2/best_offer', OfferView.as_view(), name='offer-get'),
    path('api/v2/best_offer', OfferView.as_view(), name='offer-post'),

    # Book service
    path('api/v2/book_serice', BookServiceView.as_view(), name='Book-service-get'),
    path('api/v2/book_serice', BookServiceView.as_view(), name='book-servie-post'),
    # path('api/v2/customer', CustomerView.as_view(), name='customer-put'),
    path('api/v2/book_serice/<int:bs_id>',Delete_BookService.as_view(),name='book-service-delete'),

    # Partner View
    path('api/v2/partner', PartnerView.as_view(), name='partner-get'),
    path('api/v2/partner', PartnerView.as_view(), name='partner-post'),
    path('api/v2/partner/<int:par_id>',Delete_Partner.as_view(),name='partner-delete'),

    # Partner Docs
    path('api/v2/partnerdocs', PartnerDocumentView.as_view(), name='partner-doc-get'),
    path('api/v2/partnerdocs', PartnerDocumentView.as_view(), name='partner-docs-post'),
    path('api/v2/partnerdocs/<int:pd_id>',Delete_PartnerDocument.as_view(),name='partner-docs-delete'),

    # Partner Portfetion Detail
    path('api/v2/partner_datail', PartnerProffetionalDetailView.as_view(), name='partner-datails-get'),
    path('api/v2/partner_datail', PartnerProffetionalDetailView.as_view(), name='partner-datails-post'),
    path('api/v2/partner_datail/<int:ppd_id>',Delete_PartnerProffetionalDetail.as_view(),name='partner-datails-delete'),


    # Partner Work Book
    path('api/v2/partner_work', PartnerWorkBookView.as_view(), name='partner-work-get'),
    path('api/v2/partner_work', PartnerWorkBookView.as_view(), name='partner-work-post'),
    path('api/v2/partner_work/<int:pwb_id>',Delete_PartnerWorkBook.as_view(),name='partner-work-delete'),


    # Partner award and portfolio
    path('api/v2/partner_award', PartnerAwardAndPhoteView.as_view(), name='partner-award-portolio-get'),
    path('api/v2/partner_award', PartnerAwardAndPhoteView.as_view(), name='partner-award-portolio-post'),
    path('api/v2/partner_award/<int:pap_id>',Delete_PartnerAwardAndPhote.as_view(),name='partner-award-portolio-delete'),


    # Partner Service Location
    path('api/v2/partnerlocaton', PartnerServiceLocationView.as_view(), name='partner-locaton-get'),
    path('api/v2/partnerlocaton', PartnerServiceLocationView.as_view(), name='partner-locaton-post'),
    path('api/v2/partnerlocaton/<int:psl_id>',Delete_PartnerServiceLocationView.as_view(),name='partner-locaton-delete'),


    # Partner Service Refrence
    path('api/v2/partnerrefrence', PartnerServiceRefrenceView.as_view(), name='partner-refrence-get'),
    path('api/v2/partnerrefrence', PartnerServiceRefrenceView.as_view(), name='partner-refrence-post'),
    path('api/v2/partnerrefrence/<int:psr1_id>',Delete_PartnerServiceRefrence.as_view(),name='partner-refrence-delete'),

    # User Review
    path('api/v2/userreview', UserReviewView.as_view(), name='user-review-get'),
    path('api/v2/userreview', UserReviewView.as_view(), name='user-review-post'),
    path('api/v2/userreview/<int:ur_id>', Delete_UserReview.as_view(), name='user-review-delete'),

    # Add to Cart
    # path('api/v2/addtocart', AddToCartView.as_view(), name='addtocart-get'),
    # path('api/v2/addtocart', AddToCartView.as_view(), name='addtocart-post'),
    # path('api/v2/addtocart/<int:ur_id>', Delete_AddToCart.as_view(), name='addtocart-delete'),

    # Order or payment gateway
    # path('api/v2/payment', PaymentGateway.as_view(), name='order-service'),
    # path('api/v2/checkout', Checkout.as_view(), name='order-checkout'),

    path('', include('adminpanel.urls')),
    path('', include('admin_api.urls')),
    path('', include('app_login.urls')),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'admin/', admin.site.urls),
    # url(r'api/', include(userapi.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
