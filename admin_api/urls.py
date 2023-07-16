from django.urls import path, include, re_path
from rest_framework import routers

from admin_api.viewsets.main_category_view import MainCategoryView
from admin_api.viewsets.category_views import CategoryView
from admin_api.viewsets.main_service_view import MainServiceView
from admin_api.viewsets.service_views import ServiceView
from admin_api.viewsets.service_about_view import AboutServiceView
from admin_api.viewsets.add_to_cart_views import AddToCartView
from admin_api.viewsets.payment_gateway import PaymentGateway, Checkout
from admin_api.viewsets.cart_view import CartView
from admin_api.viewsets.address_view import AddressView
from admin_api.viewsets.get_order_basis_of_user import CustomerOrderGetView
from admin_api.viewsets.created_order import CreatedOrderView, OrderGetView
from admin_api.viewsets.order_accept_view import OrderAcceptanceAPiView
from admin_api.viewsets.offer_api_view import BestOfferView
from admin_api.viewsets.why_serice_view import WhyServiceView

main_cat_router = routers.DefaultRouter()
main_cat_router.register(r'^main-category', MainCategoryView, basename='main-category')

cat_router = routers.DefaultRouter()
cat_router.register(r'^category', CategoryView, basename='category')

main_service_router = routers.DefaultRouter()
main_service_router.register(r'^main-service', MainServiceView, basename='main-service')

service_router = routers.DefaultRouter()
service_router.register(r'^service', ServiceView, basename='service')

about_service_router = routers.DefaultRouter()
about_service_router.register(r'^about-service', AboutServiceView, basename='about-service')

cart_router = routers.DefaultRouter()
cart_router.register(r'^cart', CartView, basename='cart')

add_to_cart_router = routers.DefaultRouter()
add_to_cart_router.register(r'^addtocart', AddToCartView, basename='about-service')

place_order = routers.DefaultRouter()
place_order.register(r'^orders', PaymentGateway, basename='orders')

handller = routers.DefaultRouter()
handller.register(r'^v1', Checkout, basename='handlerequest')

address = routers.DefaultRouter()
address.register(r"^address", AddressView, basename="address")

get_order = routers.DefaultRouter()
get_order.register(r'^get_order', CreatedOrderView)

get_offer = routers.DefaultRouter()
get_offer.register(r'^offer_view', BestOfferView, basename="offer_view")

why_service = routers.DefaultRouter()
why_service.register(r'^why_service', WhyServiceView, basename="why_service")

urlpatterns = [
    re_path(r'^api/v1/', include(main_cat_router.urls)),
    re_path(r'^api/v1/', include(cat_router.urls)),
    re_path(r'^api/v1/', include(main_service_router.urls)),
    re_path(r'^api/v1/', include(service_router.urls)),
    re_path(r'^api/v1/', include(about_service_router.urls)),
    re_path(r'^api/v1/', include(cart_router.urls)),
    re_path(r'^api/v1/', include(add_to_cart_router.urls)),
    re_path(r'^api/v1/', include(place_order.urls)),
    re_path(r'^api/', include(handller.urls)),
    re_path(r'^api/v1/', include(address.urls)),
    re_path(r'^api/v1/', include(get_order.urls)),
    re_path(r'^api/v1/', include(get_offer.urls)),
    re_path(r'^api/v1/', include(why_service.urls)),
    path('api/v1/customer_order/<int:id>/', CustomerOrderGetView.as_view({'get': 'get'}), name='customer_order-detail'),
    path('api/v1/vender_order_get/<int:id>/', OrderGetView.as_view({'get': 'get_order_basis_of_vender'}), name='get_order_basis_of_vender'),
    path('api/v1/customer_order_get/<int:id>/', OrderGetView.as_view({'get': 'get_order_basis_of_customer'}), name='get_order_basis_of_customer'),
    path('api/v2/order_accept', OrderAcceptanceAPiView.as_view(), name='order_accept'),
]

