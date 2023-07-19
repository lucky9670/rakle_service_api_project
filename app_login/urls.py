from django.urls import path, include, re_path, re_path
from app_login.all_customer_views import CustomerView, CustomerLoginView, CustomerUpdateView, CustomerGetView, CustomerOneView, CustomerImageUpdateView
from app_login.user_api import RegisterAPI, LoginAPI, logout, ChangePassword, Forgetpassword, ResetPassword
from app_login.vender_profile import BankUpdateView, GeneralUpdateView, ImageUpdateView
from app_login.frenchiser_details_views import FranchieserBankUpdateView, FranchieserGeneralUpdateView, FranchieserImageUpdateView
from rest_framework import routers
from app_login.viewsets.request_money_viewsets import VenderRequestMoneyViews, FanchaiserRequestMoneyViews

bank_update = routers.DefaultRouter()
bank_update.register(r'^bank_upadate', BankUpdateView, basename='bank_upadate')

basic_update = routers.DefaultRouter()
basic_update.register(r'^basic_upadate', GeneralUpdateView, basename='basic_upadate')

image_update = routers.DefaultRouter()
image_update.register(r'^image_upadate', ImageUpdateView, basename='image_upadate')

franchieser_bank_update = routers.DefaultRouter()
franchieser_bank_update.register(r'^f_bank_upadate', FranchieserBankUpdateView, basename='franchieser_bank_upadate')

franchieser_basic_update = routers.DefaultRouter()
franchieser_basic_update.register(r'^f_basic_upadate', FranchieserGeneralUpdateView, basename='franchieser_basic_upadate')

franchieser_image_update = routers.DefaultRouter()
franchieser_image_update.register(r'^f_image_upadate', FranchieserImageUpdateView, basename='franchieser_image_upadate')

vender_request_money = routers.DefaultRouter()
vender_request_money.register(r'^vender_request_money', VenderRequestMoneyViews, basename='vender_request_money')

franchaiser_request_money = routers.DefaultRouter()
franchaiser_request_money.register(r'^franchaiser_request_money', FanchaiserRequestMoneyViews, basename='franchaiser_request_money')


urlpatterns = [
    path('api/v2/customer-register', CustomerView.as_view(), name='customer-registration'),
    path('api/v2/customer-get', CustomerGetView.as_view(), name='customer-get'),
    path('api/v2/customer-get/<int:id>',CustomerOneView.as_view({'get':'get_customer'}),name='customer_get'),
    path('api/v2/customer-login', CustomerLoginView.as_view(), name='customer-login'),
    path('api/v2/customer-update', CustomerUpdateView.as_view(), name='customer-update'),
    path('api/v2/customer-image-update', CustomerImageUpdateView.as_view(), name='customer-image-update'),

    path('api/Account/logout',logout.as_view(),name='logout'),
    path('api/Account/register', RegisterAPI.as_view(), name='register'),
    path('api/Account/login', LoginAPI.as_view(), name='login'),
    path('api/Account/change_password', ChangePassword.as_view(), name='change_password'),
    path('api/Account/forgate_password', Forgetpassword.as_view(), name='forgate_password'),
    path('api/Account/reset_password', ResetPassword.as_view(), name='reset_password'),
    re_path(r'^api/v1/', include(bank_update.urls)),
    re_path(r'^api/v1/', include(basic_update.urls)),
    re_path(r'^api/v1/', include(image_update.urls)),
    re_path(r'^api/v1/', include(franchieser_bank_update.urls)),
    re_path(r'^api/v1/', include(franchieser_basic_update.urls)),
    re_path(r'^api/v1/', include(franchieser_image_update.urls)),
    re_path(r'^api/v1/', include(vender_request_money.urls)),
    re_path(r'^api/v1/', include(franchaiser_request_money.urls)),
]