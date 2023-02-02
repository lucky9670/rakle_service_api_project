from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catagory, name="catagory"),
    path('category/delete/<int:n>', views.catdelete, name="catagorydelete"),
    path('category/edit/<int:n>', views.catedit, name="catagoryedit"),
    path('subcat/', views.subcat, name="subcat"),
    path('subcat/delete/<int:n>', views.subcatdelete, name="subcatdelete"),
    path('subcat/edit/<int:n>', views.subcatedit, name="subcatedit1"),
    path('mainservice/', views.mainservice, name="mainservice"),
    path('mainservice/delete/<int:n>', views.mainservicedelete, name="mainservicedelete"),
    path('mainservice/edit/<int:n>', views.mainserviceedit, name="mainserviceedit"),
    path('service/', views.service1, name="service"),
    path('service/delete/<int:n>', views.servicedelete, name="servicedelete"),
    path('service/edit/<int:n>', views.serviceedit, name="editservice"),
    path('loadmainct/', views.loadmainct, name="loadmainct"),
    path('loadmainct1/', views.loadmainct1, name="loadmainctser"),
    path('bestoffer/', views.bestoffer, name="bestoffer"),
]