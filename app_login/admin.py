from django.contrib import admin
from .models import UserSignupModel, AllCustomer, CustomerDevice, VenderProfile, FranchieserProfile
# Register your models here.

# @admin.register(UserSignupModel)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'name', 'age', 'username', 'address','phone_number','gender']
admin.site.register(UserSignupModel)
admin.site.register(CustomerDevice)
admin.site.register(VenderProfile)
admin.site.register(FranchieserProfile)

@admin.register(AllCustomer)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", 'phone','password', 'otp', 'name']
    #  'first_name', 'last_name', 'phone_number', 'address', 'otp_type', 'user_type'




    