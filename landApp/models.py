from datetime import timedelta,datetime
import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class Product(models.Model):
    productName=models.CharField(max_length=255)
    quantity=models.IntegerField(default=1)
    description=models.TextField(default='')

    def __str__(self) -> str:
        return str(self.productName)



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullName=models.CharField(max_length=255)
    
    profileImage=models.ImageField(upload_to='borderImages/')
    userType=models.CharField(max_length=255,default='Normal User')
    number=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    status=models.BooleanField(default=True)


    def save(self,*args,**kwargs):
        ReportInfo.objects.create(reportTitle='New User was registred',desc='user fullName'+self.fullName)
        # self.save()
        return super().save()
    def theImage(self):
        if self.profileImage:
            return mark_safe('<img src={} width="100px" >'.format(self.profileImage.url))
        else:
            return mark_safe('<img src={} width="100px" >'.format('https://st3.depositphotos.com/3581215/18899/v/450/depositphotos_188994514-stock-illustration-vector-illustration-male-silhouette-profile.jpg')) 
    theImage.allow_tags=True
    def __str__(self) -> str:
        return str(self.fullName)



def generateRandomReffralCode():
    randomNum ='borderId_'+str(UserProfile.objects.last().pk+1)
    return randomNum
   

def three_month_from_today():
    return datetime.now() + timedelta(days=60)


COUNTRY_LIST = (
    ('somalia','SOMALIA'),
    ('united state', 'UNITED STATE'),
    ('kenya', 'KENYA'),
    ('united state', 'UNITED STATE'),
    ('united state', 'UNITED STATE'),
    ('united state', 'UNITED STATE'),
    ('united state', 'UNITED STATE'),
    ('united state', 'UNITED STATE'),
)

class BorderRegistration(models.Model):
    porderGeneratedId=models.CharField(max_length=255,default=generateRandomReffralCode())
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    passportId=models.CharField(max_length=266,default='')
    fromCountry=models.CharField(max_length=255,choices=COUNTRY_LIST,default='somalia')
    idCardNo=models.CharField(max_length=255)
    expireDate=models.DateTimeField(default=three_month_from_today)
    userState=models.CharField(max_length=255)
    userAddress=models.CharField(max_length=555)
    enteringDate=models.DateTimeField()
    nationality=models.CharField(max_length=255)
    fingerPrintCD=models.CharField(max_length=10000,default='')
    registrationDate=models.DateTimeField(auto_now=True)
    userProducts=models.ManyToManyField(Product,null=True,blank=True)   

    def save(self,*args,**kwargs):
        ReportInfo.objects.create(reportTitle='New border was registred to this '+self.theUser.fullName,desc='message was sended'+self.idCardNo)
        # self.save()
        return super().save()
    def __str__(self) -> str:
        return str(self.idCardNo)


    

class MessagesFor(models.Model):
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    messageTitle=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now=True)
    fullText=models.TextField()
    datetime=models.DateTimeField(null=True,blank=True)

    def save(self,*args,**kwargs):
        ReportInfo.objects.create(reportTitle='New message was sended to this '+self.theUser.fullName,desc='message was sended'+self.fullText)
        # self.save()
        return super().save()
    
    def __str__(self) -> str:
        return str(self.messageTitle)



class ReportInfo(models.Model):
    reportTitle=models.CharField(max_length=255)
    desc=models.TextField(null=True,blank=True)
    datetime=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.reportTitle)