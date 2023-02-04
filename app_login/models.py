from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SignUpManager(BaseUserManager):
    def create_user(self, email, username, age, name, password=None):
        if not email:
            raise ValueError("insert user")
        if not username:
            raise ValueError("insert username")
        if not name:
            raise ValueError("insert name")
        if not age:
            raise ValueError("insert age")
        user = self.model(email=self.normalize_email(email),username=username,age=age,name=name,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, age, name, password):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            age=age,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserSignupModel(AbstractBaseUser):
    GENDER = [('male', 'Male'),
                ('famal', 'Femal'),
                ('other', 'Other')]
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    age = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=500)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    gender = models.CharField(max_length=50, null=False, choices=GENDER, default='unknown')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name", "age",]
    objects = SignUpManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    
class AllCustomer(AbstractBaseUser):
    phone = models.CharField(unique=True, max_length=15)
    name = models.CharField(max_length=250, default='')
    gender = models.CharField(max_length=10, default='')
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