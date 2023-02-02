from django.contrib import admin
from .models import UserSignupModel
# Register your models here.

@admin.register(UserSignupModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'age', 'username', 'address','phone_number','gender']
    #  'first_name', 'last_name', 'phone_number', 'address', 'otp_type', 'user_type'




    