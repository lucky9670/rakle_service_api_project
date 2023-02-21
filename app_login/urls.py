from django.urls import path, include
from app_login.all_customer_views import CustomerView, CustomerLoginView, CustomerUpdateView
from app_login.user_api import RegisterAPI, LoginAPI, logout
from app_login.vender_profile import BankUpdateView, GeneralUpdateView, ImageUpdateView
from rest_framework import routers
from django.conf.urls import  url


bank_update = routers.DefaultRouter()
bank_update.register(r'^bank_upadate', BankUpdateView, basename='bank_upadate')

basic_update = routers.DefaultRouter()
basic_update.register(r'^basic_upadate', GeneralUpdateView, basename='basic_upadate')

image_update = routers.DefaultRouter()
image_update.register(r'^image_upadate', ImageUpdateView, basename='image_upadate')

urlpatterns = [
    path('api/v2/customer-register', CustomerView.as_view(), name='customer-registration'),
    path('api/v2/customer-login', CustomerLoginView.as_view(), name='customer-login'),
    path('api/v2/customer-update', CustomerUpdateView.as_view(), name='customer-update'),

    path('api/Account/logout',logout.as_view(),name='logout'),
    path('api/Account/register', RegisterAPI.as_view(), name='register'),
    path('api/Account/login', LoginAPI.as_view(), name='login'),
    url(r'^api/v1/', include(bank_update.urls)),
    url(r'^api/v1/', include(basic_update.urls)),
    url(r'^api/v1/', include(image_update.urls)),
]