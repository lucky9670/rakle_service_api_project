from django.urls import path, include, re_path, re_path
from app_login.all_customer_views import CustomerView, CustomerLoginView, CustomerUpdateView, CustomerGetView, CustomerOneView, CustomerImageUpdateView
from app_login.user_api import RegisterAPI, LoginAPI, logout
from app_login.vender_profile import BankUpdateView, GeneralUpdateView, ImageUpdateView
from rest_framework import routers


bank_update = routers.DefaultRouter()
bank_update.register(r'^bank_upadate', BankUpdateView, basename='bank_upadate')

basic_update = routers.DefaultRouter()
basic_update.register(r'^basic_upadate', GeneralUpdateView, basename='basic_upadate')

image_update = routers.DefaultRouter()
image_update.register(r'^image_upadate', ImageUpdateView, basename='image_upadate')

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
    re_path(r'^api/v1/', include(bank_update.urls)),
    re_path(r'^api/v1/', include(basic_update.urls)),
    re_path(r'^api/v1/', include(image_update.urls)),
]