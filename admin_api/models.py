import email
from email.mime import image
from pyexpat import model
from unicodedata import name
from django.db import models
from lib.models import BaseModel
from django.utils.translation import gettext_lazy as _
# from .constants import PaymentStatus
from django.utils import timezone
from app_login.models import UserSignupModel

# Create your models here.

class MainCategory(BaseModel):
    main_cat_name = models.CharField(max_length=500)
    status =models.BooleanField(default=True)
    main_cat_image = models.ImageField(upload_to='main_category',blank=False, null=False)

    def __str__(self):
         return self.main_cat_name

class Category(BaseModel):
    main_cat_name = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=500)
    status =models.BooleanField(default=False)
    cat_image = models.ImageField(upload_to='category',blank=False, null=False)
    def __str__(self):
         return self.cat_name

class MainService(BaseModel):
    main_cat_name = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_service_name = models.CharField(max_length=500)
    status =models.BooleanField(default=False)
    main_service_image = models.ImageField(upload_to='main_service',blank=False, null=False)
    def __str__(self):
         return self.main_service_name


class Service(BaseModel):
    main_cat_name = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_service_name = models.ForeignKey(MainService, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=500)
    status =models.BooleanField(default=False)
    service_image = models.ImageField(upload_to='service',blank=False, null=False)
    service_charge = models.CharField(max_length=1000)
    service_time = models.CharField(max_length=1000)
    discount = models.CharField(max_length=1000)
    def __str__(self):
         return self.service_name

class Package(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    queestion = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)

class AboutService(BaseModel):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='service_about', blank=False, null=False)
    video = models.CharField(max_length=1000)
    discription = models.CharField(max_length=10000)
    notes = models.CharField(max_length=1000)



class Slider(models.Model):
    image = models.FileField(upload_to='slider',blank=False, null=False)
    text = models.CharField(max_length=500, blank=True, null=True)


class City(models.Model):
    city_name = models.CharField(max_length=500)
    city_state =models.CharField(max_length=500)
    city_countory = models.CharField(max_length=500)
    transdate = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)

class Customer(models.Model):
    customer_name = models.CharField(max_length=500)
    customer_gender =models.CharField(max_length=500)
    customer_email = models.EmailField(max_length=500)
    customer_phone = models.CharField(max_length=1000)
    customer_street = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class BookService(models.Model):
    bookser_date = models.DateField(null=True, blank=True)
    bookser_time = models.TimeField(null=True, blank=True)
    bookser_remark =models.CharField(max_length=255)
    payment_method =models.CharField(max_length=55)
    transdate =models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

class Partner(models.Model):
    partner_name = models.CharField(max_length=500)
    partner_image =models.CharField(max_length=500)
    partner_image_url = models.CharField(max_length=500)
    partner_gender =models.CharField(max_length=500)
    partner_email = models.EmailField(max_length=500)
    partner_phone = models.CharField(max_length=1000)
    partner_proffetion = models.CharField(max_length=1000)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    transdate = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)

class PartnerDocument(models.Model):
    document_name = models.CharField(max_length=500)
    document_file =models.CharField(max_length=500)
    father_name = models.CharField(max_length=500)
    date_of_birth =models.DateField()
    street_address = models.CharField(max_length=255)
    partner_city = models.ForeignKey(City, on_delete=models.CASCADE)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)

class PartnerProffetionalDetail(models.Model):
    business_card = models.CharField(max_length=500)
    business_name =models.CharField(max_length=500)
    alternate_mobile = models.CharField(max_length=500)
    alternate_email = models.EmailField(max_length=500)
    proffetinal_experience = models.CharField(max_length=1000)
    type_of_dealer = models.CharField(max_length=1000)
    service_provoided = models.CharField(max_length=1000)
    minimum_warranty = models.CharField(max_length=1000)
    website_link = models.CharField(max_length=1000, blank=True, null=True)
    company_intro = models.CharField(max_length=1000, blank=True, null=True)
    transdate = models.CharField(max_length=1000)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

class PartnerWorkBook(models.Model):
    pwb_image = models.CharField(max_length=255)
    transdate = models.CharField(max_length=1000)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

class PartnerAwardAndPhote(models.Model):
    pap_name = models.CharField(max_length=255)
    pap_image = models.CharField(max_length=255)
    transdate = models.CharField(max_length=1000)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

class PartnerServiceLocation(models.Model):
    pap_location = models.CharField(max_length=255)
    transdate = models.CharField(max_length=1000)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)


class PartnerServiceRefrence(models.Model):
    refrence_name = models.CharField(max_length=255)
    refrence_dec = models.CharField(max_length=255)
    transdate = models.CharField(max_length=1000)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)


class VideoConsultation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

class BestOffer(models.Model):
    name = models.CharField(max_length=100)
    offerimage = models.FileField(upload_to='offer',blank=False, null=False)
    offer = models.CharField(max_length=100)

class UserReview(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

# Add to Cart
class AddToCart(BaseModel):
    user = models.ForeignKey(UserSignupModel, on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    service_quantity = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"

class Order(models.Model):
    status_choices = (
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    )
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices, default=1)

    total_amount = models.FloatField()
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email + " " + str(self.id)
