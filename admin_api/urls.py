from django.urls import path, include
from django.conf.urls import  url
from rest_framework import routers

from admin_api.viewsets.main_category_view import MainCategoryView
from admin_api.viewsets.category_views import CategoryView
from admin_api.viewsets.main_service_view import MainServiceView
from admin_api.viewsets.service_views import ServiceView


main_cat_router = routers.DefaultRouter()
main_cat_router.register(r'^main-category', MainCategoryView, basename='main-category')

cat_router = routers.DefaultRouter()
cat_router.register(r'^category', CategoryView, basename='category')

main_service_router = routers.DefaultRouter()
main_service_router.register(r'^main-service', MainServiceView, basename='main-service')

service_router = routers.DefaultRouter()
service_router.register(r'^service', ServiceView, basename='service')


urlpatterns = [
    url(r'^api/v1/', include(main_cat_router.urls)),
    url(r'^api/v1/', include(cat_router.urls)),
    url(r'^api/v1/', include(main_service_router.urls)),
    url(r'^api/v1/', include(service_router.urls)),
]

