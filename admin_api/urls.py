from django.urls import path, include
from django.conf.urls import  url
from rest_framework import routers

from admin_api.viewsets.main_category_view import MainCategoryView
from admin_api.viewsets.category_views import CategoryView
from admin_api.viewsets.main_service_view import MainServiceView
from admin_api.viewsets.service_views import ServiceView
from admin_api.viewsets.service_about_view import AboutServiceView
from admin_api.viewsets.add_to_cart_views import AddToCartView


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

add_to_cart_router = routers.DefaultRouter()
add_to_cart_router.register(r'^addtocart', AddToCartView, basename='about-service')


urlpatterns = [
    url(r'^api/v1/', include(main_cat_router.urls)),
    url(r'^api/v1/', include(cat_router.urls)),
    url(r'^api/v1/', include(main_service_router.urls)),
    url(r'^api/v1/', include(service_router.urls)),
    url(r'^api/v1/', include(about_service_router.urls)),
    url(r'^api/v1/', include(add_to_cart_router.urls)),
]

