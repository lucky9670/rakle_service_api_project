from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, UserManager
from django.db.models.deletion import DO_NOTHING
from lib.models import BaseModel


# class SignUpManager(BaseUserManager):
#     def create_user(self, phone, password=None):
#         if not phone:
#             raise ValueError("insert phone")
#         # if not username:
#         #     raise ValueError("insert username")
    
#         user = self.model(phone=phone)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phone, password):

#         user = self.create_user(
#             phone=phone,
#             # username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class UserSignupModel(AbstractUser):
    ADMIN = 1
    FRANCHISER = 2
    VENDER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (FRANCHISER, 'Franchiser'),
        (VENDER, 'Vender')
    )
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'username']
    """
        Inherits from default User of Django and extends the fields.
        The following fields are part of Django User Model:
        | id
        | password
        | last_login
        | is_superuser
        | username
        | first_name
        | last_name
        | email
        | is_staff
        | is_active
        | date_joined
        """
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20, unique=True, null=False, db_index=True, error_messages={
        'unique': "Phone Number already exists"
    })
    # username = models.CharField(max_length=15, unique=True)
    franchiser = models.ForeignKey("self",related_name="parent",on_delete=DO_NOTHING,null=True,blank=True)
    role =  models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    otp = models.CharField(max_length=30, default='')

    objects_original = UserManager()
    def __str__(self):
        return self.name + self.phone

    @property
    def to_json(self):
        _to_json = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'name':self.name,
        }
        return _to_json
    
class AllCustomer(AbstractBaseUser):
    phone = models.CharField(unique=True, max_length=15)
    name = models.CharField(max_length=250, default='')
    gender = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to="customer", blank=False, null=False)
    otp = models.CharField(max_length=30)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone', ]

    def __str__(self):
        return self.phone

class CustomerManager(BaseUserManager):
    def create_user(self, phone, password=None):
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomerDevice(BaseModel):
    web_id = models.CharField(max_length=250)
    app_id = models.CharField(max_length=250)


class VenderProfile(BaseModel):
    user = models.ForeignKey(UserSignupModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=50 ,blank=True, null=True)
    latitude = models.CharField(max_length=50 ,blank=True, null=True)
    longitude = models.CharField(max_length=50 ,blank=True, null=True)
    image = models.ImageField(upload_to='vender_profile',blank=True, null=True)
    aadhar_card = models.CharField(max_length=50 ,blank=True, null=True)
    pan_card = models.CharField(max_length=50 ,blank=True, null=True)
    account_number = models.CharField(max_length=50 ,blank=True, null=True)
    ifsc_code = models.CharField(max_length=50 ,blank=True, null=True)
    account_holder = models.CharField(max_length=50 ,blank=True, null=True)
    bank_name = models.CharField(max_length=50 ,blank=True, null=True)
    branch = models.CharField(max_length=50 ,blank=True, null=True)
    qualification = models.CharField(max_length=50 ,blank=True, null=True)
    age = models.CharField(max_length=50 ,blank=True, null=True)
    gender = models.CharField(max_length=50 ,blank=True, null=True)
    status = models.BooleanField(default=True)
    notification_id = models.CharField(max_length=100 ,blank=True, null=True)
    email = models.CharField(max_length=254 ,blank=True, null=True)
    amount = models.FloatField(default=0)
    no_of_vender = models.IntegerField(blank=True, null=True)

class FranchieserProfile(BaseModel):
    user = models.ForeignKey(UserSignupModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='franchieser_profile',blank=True, null=True)
    aadhar_card = models.CharField(max_length=50, blank=True, null=True)
    pan_card = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=50, blank=True, null=True)
    account_holder = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)
    notification_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    amount = models.FloatField(default=0)
    no_of_vender = models.IntegerField(blank=True, null=True)

