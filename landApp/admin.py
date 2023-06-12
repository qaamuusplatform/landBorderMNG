from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('fullName','theImage','user','userType','number','username','status')
    # ordering: 
    search_fields=('fullName','number','username','status')

@admin.register(BorderRegistration)
class BorderRegistrationAdmin(admin.ModelAdmin):
    list_display=('theUser','idCardNo','expireDate','userState','userAddress','enteringDate','nationality','fingerPrintCD','remainTime')
    # ordering: 
    search_fields=('fingerPrintCD','nationality','userAddress')

@admin.register(MessagesFor)
class MessagesForAdmin(admin.ModelAdmin):
    list_display=('theUser','messageTitle','date','fullText')
    # ordering: 
    search_fields=('messageTitle','fullText','date')
