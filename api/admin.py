from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','productName','quantity','description')
    # ordering: 
    search_fields=('id','productName','quantity','description')

admin.register(ReportInfo)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('fullName','theImage','userType','number','username')
    # ordering: 
    search_fields=('fullName','number','username')

@admin.register(BorderRegistration)
class BorderRegistrationAdmin(admin.ModelAdmin):
    list_display=('theUser','idCardNo','userState','userAddress','enteringDate','nationality','expireDate')
    # ordering: 
    search_fields=('fingerPrintCD','nationality','userAddress')

@admin.register(MessagesFor)
class MessagesForAdmin(admin.ModelAdmin):
    list_display=('theUser','messageTitle','date','fullText')
    # ordering: 
    search_fields=('messageTitle','fullText','date')


@admin.register(ReportInfo)
class ReportInfoAdmin(admin.ModelAdmin):
    list_display=('reportTitle','desc','datetime')
    # ordering: 
    search_fields=('reportTitle','desc','datetime')
