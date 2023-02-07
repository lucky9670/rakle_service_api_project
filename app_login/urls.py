from django.urls import path
from app_login.all_customer_views import CustomerView, CustomerLoginView, CustomerUpdateView

urlpatterns = [
    path('api/v2/customer-register', CustomerView.as_view(), name='customer-registration'),
    path('api/v2/customer-login', CustomerLoginView.as_view(), name='customer-login'),
    path('api/v2/customer-update', CustomerUpdateView.as_view(), name='customer-update'),
]