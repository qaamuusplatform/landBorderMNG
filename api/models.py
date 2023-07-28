from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils.safestring import mark_safe

# Create your models here.
class Product(models.Model):
    productName=models.CharField(max_length=255)
    quantity=models.IntegerField(default=1)
    description=models.TextField(default='')

    def __str__(self) -> str:
        return str(self.productName)



class UserProfile(models.Model):
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255,default='12345')
    is_superuser=models.BooleanField(default=False)
    theUser=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    fullName=models.CharField(max_length=255,default="")
    gender=models.CharField(max_length=255,default='Male')
    fingerPrintCode=models.TextField(null=True,blank=True)
    faceDetected=models.FileField(upload_to='usersFaceDetected/',null=True,blank=True)
    profileImage=models.ImageField(upload_to='borderImages/',null=True,blank=True)
    userType=models.CharField(max_length=255,default='Normal User')
    number=models.CharField(max_length=255,default="252")
    status=models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if self.theUser==None:
            user=User.objects.filter(username=self.username)
            if user.exists():
                print('exist')
                user=user.first()
                user.username=self.username
                user.is_active=True
                user.save()
                self.theUser=user
            else:
                print('not ')
                newUser=User.objects.create(username=self.username)
                print('created ')
                newUser.set_password(self.password)
                newUser.is_superuser=self.is_superuser
                newUser.is_active=True
                newUser.save()
                self.theUser=newUser


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

class BorderRegistration(models.Model):
    borderGeneratedId=models.CharField(max_length=255,default="0")
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    idCardNo=models.CharField(max_length=255)
    expireDate=models.DateTimeField(null=True,blank=True)
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


class ScannedFaceDt(models.Model):
    imageName=models.CharField(max_length=255)
    scannedImage=models.FileField(upload_to='scannedImage/',null=True,blank=True)


    
class FingerPrintScanDt(models.Model):
    fingerPrintCode=models.TextField(null=True,blank=True)
    fingerPrintImage=models.FileField(upload_to='scannedFingers/', null=True, blank=True, default='fingerprint.jpg')
