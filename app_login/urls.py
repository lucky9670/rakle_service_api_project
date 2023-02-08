from django.urls import path
from app_login.all_customer_views import CustomerView, CustomerLoginView, CustomerUpdateView
from app_login.user_api import RegisterAPI, LoginAPI, logout

urlpatterns = [
    path('api/v2/customer-register', CustomerView.as_view(), name='customer-registration'),
    path('api/v2/customer-login', CustomerLoginView.as_view(), name='customer-login'),
    path('api/v2/customer-update', CustomerUpdateView.as_view(), name='customer-update'),

    path('api/Account/logout',logout.as_view(),name='logout'),
    path('api/Account/register', RegisterAPI.as_view(), name='register'),
    path('api/Account/login', LoginAPI.as_view(), name='login'),
]