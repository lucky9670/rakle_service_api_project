from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from admin_api.serialization.work_serializer import *
from rackle import settings
from admin_api.models import *
from app_login.models import VenderProfile
from drf_yasg.utils import swagger_auto_schema
from admin_api.serialization.update_serializer import *
from admin_api.serialization.paymentserializer import *
import razorpay
from django.contrib.sites.shortcuts import get_current_site
from datetime import datetime
from geopy.distance import geodesic
from fcm_django.models import FCMDevice

def calculate_distance(lat1, lon1, lat2, lon2):
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    distance = geodesic(point1, point2).kilometers
    return distance

def get_users_within_circle(center_latitude, center_longitude, radius_km=5.0):
    users_within_circle = []
    all_users = VenderProfile.objects.all()
    for user in all_users:
        distance = calculate_distance(center_latitude, center_longitude, user.latitude, user.longitude)
        if distance <= radius_km:
            users_within_circle.append(user)
    return users_within_circle


class PaymentGateway(ViewSet):
    serializer_class = OrderSerializer
   
    @swagger_auto_schema(tags=['Order'], request_body=OrderSerializer)
    def create(self, request, *args, **kwargs):
        client = razorpay.Client(auth=(settings.razorpay_api_key, settings.razorpay_api_secret_key))
        check_data = request.data
        address = check_data['address']
        customer = check_data['customer']
        cart_detail = check_data['cart_detail']
        delivery_date = check_data['delivery_date']
        time_slot = check_data['time_slot']
        total_amount = check_data['total_amount']
        print(check_data)
        time_slot = datetime.strptime(time_slot, "%H:%M:%S").time()
        # try:
        address = Address.objects.get(id=int(address))
        customer = AllCustomer.objects.get(id=int(customer))
        cart_detail = AddToCart.objects.get(id=int(cart_detail))
        # except:
        #     address = Address.objects.create()
        # for service, service_quantity in zip(services, service_quantities):
        order = Order.objects.create(address = address, customer = customer, cart_detail = cart_detail, delivery_date= delivery_date, time_slot=time_slot, total_amount=0, payment_status=3, delevery_status=1)
        razorpay_order = client.order.create({"amount": total_amount*100, "currency": "INR", "payment_capture": 1})
        callback_url = 'http://'+ str(get_current_site(request))+"/api/v1/handlerequest/"
        # user = AllCustomer.objects.get(id= int(customer))
        order.order_id = razorpay_order['id']
        order.razorpay_order_id = razorpay_order['id']
        order.total_amount = total_amount
        order.save()

        context = {
            "api_key" : settings.razorpay_api_key,
            "order_id" : razorpay_order['id'],
            "name" : customer.name,
            "email" : customer.gender,
            "phone" : customer.phone,
            "amount" : total_amount,
            'callback_url':callback_url
        }
        # print(context)
        return Response({
            "order": context,
        })
    

class Checkout(ViewSet):
    serializer_class = CheckoutSerializer
   
    @swagger_auto_schema(tags=['Order'])
    @action(detail=False, methods=["POST"])
    def handlerequest(self, request, *args, **kwargs):
        payment_id = request.data['razorpay_payment_id']
        order_id = request.data['razorpay_order_id']
        signature = request.data['razorpay_signature']
        params_dict = { 
        'razorpay_order_id': order_id, 
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
        }
        client = razorpay.Client(auth=(settings.razorpay_api_key, settings.razorpay_api_secret_key))
        try:
            order_db = Order.objects.get(order_id=order_id)
            ser_detail = AddToCart.objects.get(id=order_db.cart_detail)
        except:
            return Response({"offer" : "505 Not Found"})
        order_db.razorpay_payment_id = payment_id
        order_db.razorpay_signature = signature
        order_db.save()
        result = client.utility.verify_payment_signature(params_dict)
        if result==True:
            amount = order_db.total_amount * 100   #we have to pass in paisa
            try:
                client.payment.capture(payment_id, amount)
                order_db.payment_status = 1
                order_db.save()
                ser_detail.checkouted =True
                ser_detail.save()
                customer = AllCustomer.objects.get(customer= order_db.order_db)
                OrderAcceptance.objects.create(customer = customer, order = order_db)
                users_within_circle = get_users_within_circle(order_db.address.latitude, order_db.address.longitude)
                for user in users_within_circle:
                    print(user.username, user.latitude, user.longitude)
                    device = FCMDevice.objects.get(user=user.id, registration_id= user.notification_id)
                    device.send_message(title="title", body="body")
                return Response({"payment_status": "Success",})
            except:
                order_db.payment_status = 2
                order_db.save()
                return Response({
                    "payment_status": "Fail",
                })
        else:
            order_db.payment_status = 2
            order_db.save()
            return Response({
                "payment_status": "Fail",
            })