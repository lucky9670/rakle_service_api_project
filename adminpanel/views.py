from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
import requests
from django.http.response import JsonResponse
import json
from django.core.files.storage import FileSystemStorage
import base64
from admin_api.models import *
from rackle import settings
import os

# Create your views here.
def catagory(request):
    # data = requests.get(url = settings.Main_Cat)
    # print(data.json())
    return render(request, 'Catagory.html')

def catdelete(request, n):
    r = requests.delete(url = (f'{settings.Main_Cat}/{n}'),data = {'id':n})
    return redirect(catagory)



def catedit(request, n):
    response = MainCategory.objects.get(id = n)

    if request.method=="POST" and request.FILES['cat_img']:
        response.main_cat_name = request.POST.get('cat_name')
        response.status = request.POST.get('status1') 
        doc = request.FILES
        myfile=doc['cat_img']
        fs = FileSystemStorage()
        filename = fs.save(f"Main_Cat/{myfile.name}", myfile)
        url1 = fs.url(filename)
        response.main_cat_image = url1
        data1={
            'main_cat_name':response.main_cat_name,
            'main_cat_image':url1,
            'status':response.status,
        }
        print(data1)
        # response.save()
        # return render(request, 'edit.html')
        r = requests.put(url = (f"{settings.Main_Cat}/{n}"), data = data1)
        url = (f"{settings.Main_Cat}/{n}")
        # print(url)
        return redirect(catagory)
    return render(request, 'edit.html', {"empdata": response})


# def createcat(request):

# ++++++++++++++++++++  Subcategory  +++++++++++++++++++++++++++++++++++++++

def subcat(request):
    if request.method=="POST" and request.FILES['sub_cat_img']:
        main_cat = request.POST.get('main_cat')
        print(main_cat)
        sub_cat = request.POST.get('sub_cat')
        print(sub_cat)
        doc = request.FILES
        myfile=doc['sub_cat_img']
        fs = FileSystemStorage()
        filename = fs.save(f"sub_Cat/{myfile.name}", myfile)
        url = fs.url(filename)
        data1 = {
            'main_cat_name':main_cat,
            'cat_name':sub_cat,
            'cat_image':url
        }
        print(data1)
        r = requests.post(url = settings.Sub_Cat, data = data1)
        url = settings.Sub_Cat
        print(url)
        emp = Category.objects.all()
        emp1 = MainCategory.objects.all()
        return render(request,"SubCatagory.html", {"sub": emp, 'cat': emp1})
    else:
        emp = Category.objects.all()
        emp1 = MainCategory.objects.all()
        return render(request,"SubCatagory.html", {"sub": emp, 'cat': emp1})


def subcatdelete(request, n):
    r = requests.delete(url = (f'{settings.Sub_Cat}/{n}'),data = {'id':n})
    return redirect(subcat)


def subcatedit(request, n):
    
    response = Category.objects.get(id = n)
    main = MainCategory.objects.all()

    if request.method=="POST" and request.FILES['cat_img']:
        main_cat_name = request.POST.get('main_cat')
        response.cat_name = request.POST.get('cat_name')
        response.status = request.POST.get('status1')
        doc = request.FILES
        myfile=doc['cat_img']
        fs = FileSystemStorage()
        filename = fs.save(f"sub_Cat/{myfile.name}", myfile)
        url1 = fs.url(filename)
        response.cat_image = url1
        data1={
            'main_cat_name':int(main_cat_name),
            'cat_name':response.cat_name,
            'cat_image':url1,
            'status':response.status,

        }
        print(data1)
        r = requests.put(url = (f"{settings.Sub_Cat}/{n}"), data = data1)
        url = (f"{settings.Sub_Cat}{n}/")
        print(url)
        return redirect(subcat)
    return render(request, 'subedit.html', {"empdata": response, "main":main})



# ++++++++++++++++++++++++++++ subcat end +++++++++++++++++++++++++++
    
def mainservice(request):
    if request.method=="POST" and request.FILES['main_ser_img']:
        main_cat = int(request.POST.get('main_cat'))
        sub_cat = int(request.POST.get('sub_cat'))
        print(sub_cat)
        main_ser = request.POST.get('main_ser')
        print(main_ser)
        doc = request.FILES
        myfile=doc['main_ser_img']
        fs = FileSystemStorage()
        filename = fs.save(f"main_ser_img/{myfile.name}", myfile)
        url = fs.url(filename)
        data1 = {
            'main_cat_name':main_cat,
            'cat_name':sub_cat,
            'main_service_name':main_ser,
            'main_service_image':url
        }
        print(data1)
        # queryset = MainService.objects.create(main_cat_name = main_cat, cat_name = sub_cat, main_service_name = main_ser, main_service_image = url)  
        # queryset.save()  
        
        r = requests.post(url = settings.main_service, data = data1)
        url = settings.Sub_Cat
        print(url)
        
        emp = Category.objects.all()
        emp1 = MainCategory.objects.all()
        emp2 = MainService.objects.all()
        
        # print(emp2)
        return render(request,"MainService.html", {"sub": emp, 'cat': emp1, 'mser':emp2})
    else:
        emp = Category.objects.all()
        emp1 = MainCategory.objects.all()
        emp2 = MainService.objects.all()
        main_cat = []
        sub_cat = []
        for i in emp2:
            print(i)
            n = i.main_cat_name.id
            m = i.cat_name.id
            i.main_cat_name
            print(n)
            a = MainCategory.objects.get(id = n)
            b = Category.objects.get(id = m)

            main_cat.append(a.main_cat_name)
            sub_cat.append(b.cat_name)

        print(main_cat)
        print(sub_cat)
        return render(request,"MainService.html", {'sub': emp, 'cat': emp1, 'mser':emp2})

def mainservicedelete(request, n):
    r = requests.delete(url = (f'{settings.main_service}/{n}'),data = {'id':n})
    return redirect(mainservice)



def mainserviceedit(request, n):

    response = MainService.objects.get(id = n)
    sub = Category.objects.all()
    main = MainCategory.objects.all()

    if request.method=="POST" and request.FILES['ser_img']:
        main_cat = int(request.POST.get('main_cat'))
        sub_cat = int(request.POST.get('sub_cat'))
        ser_name = request.POST.get('ser_name')
        status = request.POST.get('status1')
        doc = request.FILES
        myfile=doc['ser_img']
        fs = FileSystemStorage()
        filename = fs.save(f"main_ser_img/{myfile.name}", myfile)
        url1 = fs.url(filename)
        
        data1={
            'main_cat_name':main_cat,
            'cat_name':sub_cat,
            'main_service_name':ser_name,
            'main_service_image':url1,
            'status':status,

        }
        print(data1)
        r = requests.put(url = (f"{settings.main_service}/{n}"), data = data1)
        url = (f"{settings.main_service}{n}/")
        print(url)
        return redirect(mainservice)
    return render(request, 'mainseredit.html', {"empdata": response, "main":main, "sub":sub})



# ------------------------- Service ------------------------------

def service1(request):

    if request.method=="POST" and request.FILES['Service_image']:
        main_cat = int(request.POST.get('main_cat'))
        sub_cat = int(request.POST.get('Sub_Cat_Name'))
        main_ser = int(request.POST.get('main_ser_name'))
        ser_name = request.POST.get('Service_Name')
        ser_video = request.POST.get('Service_video')
        ser_time = request.POST.get('Service_time')
        ser_discount = request.POST.get('Service_dis')
        doc = request.FILES
        myfile=doc['Service_image']
        fs = FileSystemStorage()
        filename = fs.save(f"ser_img/{myfile.name}", myfile)
        url = fs.url(filename)
        data1 = {
            'main_cat_name':main_cat,
            'cat_name':sub_cat,
            'main_service_name':main_ser,
            'service_name':ser_name,
            'service_charge':ser_video,
            'service_time':ser_time,
            'discount':ser_discount,
            'service_image':url
        }
        print(data1)
        r = requests.post(url = settings.service, data = data1)
        url = settings.Sub_Cat
        print(url)
        
        emp1 = MainCategory.objects.all()
        emp = Category.objects.all()
        emp2 = MainService.objects.all()
        emp3 = Service.objects.all()
        # print(emp2)
        return render(request,"Service.html", {"sub": emp, 'cat': emp1, 'mser':emp2, "ser":emp3})
    else:
        emp = Category.objects.all()
        emp1 = MainCategory.objects.all()
        emp2 = MainService.objects.all()
        emp3 = Service.objects.all()
        # print(emp2)
        return render(request,"Service.html", {'sub': emp, 'cat': emp1, 'mser':emp2, 'ser':emp3})


def servicedelete(request, n):
    r = requests.delete(url = (f'{settings.service}/{n}'),data = {'id':n})
    return redirect(service1)

def serviceedit(request, n):

    response = Service.objects.get(id = n)
    service = MainService.objects.all()
    sub = Category.objects.all()
    main = MainCategory.objects.all()

    if request.method=="POST" and request.FILES['ser_img']:
        main_cat = int(request.POST.get('main_cat'))
        sub_cat = int(request.POST.get('sub_cat'))
        main_ser = int(request.POST.get('main_ser'))
        ser_name = request.POST.get('ser_name')
        ser_video = request.POST.get('ser_video')
        ser_time = request.POST.get('ser_time')
        ser_discount = request.POST.get('ser_dis')
        status = request.POST.get('status1')
        doc = request.FILES
        myfile=doc['ser_img']
        fs = FileSystemStorage()
        filename = fs.save(f"main_ser_img/{myfile.name}", myfile)
        url1 = fs.url(filename)
        
        data1 = {
            'main_cat_name':main_cat,
            'cat_name':sub_cat,
            'main_service_name':main_ser,
            'service_name':ser_name,
            'service_charge':ser_video,
            'service_time':ser_time,
            'discount':ser_discount,
            'status':status,
            'service_image':url1
        }
        print(data1)
        r = requests.put(url = (f"{settings.service}/{n}"), data = data1)
        url = (f"{settings.service}{n}/")
        print(url)
        return redirect(service1)
    return render(request, 'serviceedit.html', {"empdata": response, "main":main, "sub":sub,'serv':service})

def loadmainct(request):
    main_cat = request.GET.get('countryid')
    print(main_cat)
    sub_cat = Category.objects.filter(main_cat_name = main_cat).all()
    print(sub_cat)
    return render(request, 'drop/maincat.html', {'subcat':sub_cat})

def loadmainct1(request):
    sub_cat = request.GET.get('catid')
    print(sub_cat)
    main_ser = MainService.objects.filter(cat_name = sub_cat).all()
    print(main_ser)
    return render(request, 'drop/catforser.html', {'subcat':main_ser})



# best offer

def bestoffer(request):
    if request.method=="POST":
        name = request.POST.get('best_name')
        offer = request.POST.get('best_offer')
        # url = request.POST.get('best_img')
        doc = request.FILES
        myfile=doc['best_img']
        # fs = FileSystemStorage()
        # filename = fs.save(f"best_offer/{myfile.name}", myfile)
        # url = fs.url(filename)
        data = {
            'name':name,
            'offer':offer,
            'offerimage':myfile
        }
        print(data)
        u  = settings.best_offer
        print(u)
        r = requests.post(url = settings.best_offer, data = data)
        # r = Student.objects.create(nam)
        bestoffer = requests.get(url = (f'{settings.best_offer}'))
        data = bestoffer.json()
        return render(request, 'bestoffer.html', {'best':data['offer']})
    
    bestoffer = requests.get(url = (f'{settings.best_offer}'))
    data = bestoffer.json()
    return render(request, 'bestoffer.html', {'best':data['offer']})
