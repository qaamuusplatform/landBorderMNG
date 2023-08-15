from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils.safestring import mark_safe

from datetime import timedelta,datetime

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
    passportID=models.CharField(max_length=255,unique=True)
    fullName=models.CharField(max_length=255,default="")
    gender=models.CharField(max_length=255,default='Male')
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
        if self._state.adding is True:
            ReportInfo.objects.create(reportTitle='New User was registred',desc='user fullName'+self.fullName)
        else:
            ReportInfo.objects.create(reportTitle=f'This User {self.fullName} was Changed',desc='user fullName'+self.fullName)
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


LANDED_TYPE_CHOICES = [
        ('By Flight', 'By Flight'),
        ('By Train', 'By Train'),
        ('By Bus', 'By Bus'),
    ]

BORDER_CURRENT_STATUS = [
        ('In', 'In The Country Flight'),
        ('Out', 'Out The Country')
    ]

REASONS = [
        ('Medical', 'Medical'),
        ('Tourisim', 'Tourisim'),
        ('Education', 'Education')
    ]

NATIONALITY = [
        ('Somalia', 'Somalia'),
        ('Somali-Land', 'Somali-Land'),
        ('Kenya', 'Kenya '),
        ('Angola', 'Angola'),
        ('Italy', 'Italy'),
    ]
def three_month_from_today():
    return datetime.now() + timedelta(days=60)   

class BorderRegistration(models.Model):
    borderGeneratedId=models.CharField(max_length=255,default="0")
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    userLandedType = models.CharField(max_length=255, choices=LANDED_TYPE_CHOICES, default='By Flight')
    subTypeLand=models.CharField(max_length=255,default='Kenya Airways')
    borderCurrentState=models.CharField(max_length=255,choices=BORDER_CURRENT_STATUS,default='In')
    enteringDate=models.DateTimeField()
    visa=models.CharField(max_length=255,default='Visa_2Month__$150')
    idCardNo=models.CharField(max_length=255)
    expireDate=models.DateTimeField(null=True,blank=True,default=three_month_from_today)
    userAddress=models.CharField(max_length=555)
    nationality=models.CharField(max_length=255,choices=NATIONALITY,default='Somalia')
    # fingerPrintCD=models.CharField(max_length=10000,default='')
    registrationDate=models.DateTimeField(auto_now=True) 
    
    reasonFor=models.CharField(max_length=255,choices=REASONS,default='Education')

    def save(self,*args,**kwargs):
        if self._state.adding:
            ReportInfo.objects.create(reportTitle='New border was registred',desc=f'New border was registred to this {self.theUser.fullName}')
        else: 
        
            oldObjectData=BorderRegistration.objects.get(pk=self.pk)
            if oldObjectData.borderCurrentState==self.borderCurrentState:
                if oldObjectData.expireDate!=self.expireDate:
                    ReportInfo.objects.create(reportTitle='Expire date changing',desc=f'The border {self.theUser.fullName} was change to his expire date to {self.expireDate}')

            else:
                if oldObjectData.expireDate!=self.expireDate:
                    ReportInfo.objects.create(reportTitle='Expire date changing',desc=f'The border {self.theUser.fullName} was change to his expire date to {self.expireDate}')
                ReportInfo.objects.create(reportTitle='The border current state was changed',desc=f'The border {self.theUser.fullName} was change to his state to {self.borderCurrentState}')

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



class Fines(models.Model):
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    fineTitle=models.CharField(max_length=255)
    fineDesc=models.TextField()
    finePrice=models.IntegerField(default=20)
    datetime=models.DateTimeField(auto_now=True)
    fixed=models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if self._state.adding:
            ReportInfo.objects.create(reportTitle=f'New fine for this border {self.theUser.fullName}',desc=f'{self.fineTitle} - {self.finePrice}')
        else: 
            if self.fixed:
                ReportInfo.objects.create(reportTitle=f'The fine for this border {self.theUser.fullName} was fixed',desc=f'{self.fineTitle} - {self.finePrice}')
        return super().save()


class ExtraTime(models.Model):
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    borderingSt=models.ForeignKey(BorderRegistration,on_delete=models.CASCADE,null=True,blank=True)
    price=models.IntegerField(default=50)
    extraDays=models.IntegerField(default=15)
    reasonForExtraDays=models.CharField(max_length=2555)
    datetime=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self._state.adding:
            latestBordering=BorderRegistration.objects.filter(theUser=self.theUser).last()
            self.borderingSt=latestBordering
            latestBordering.expireDate=latestBordering.expireDate+timedelta(days=self.extraDays)
            latestBordering.save()
            ReportInfo.objects.create(reportTitle=f'Extra Days for this border {self.theUser.fullName}',desc=f'This user requested {self.extraDays} days  for this reason {self.reasonForExtraDays} and also he/she paided the price {self.price}')
        return super().save()
