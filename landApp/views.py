from django.shortcuts import render
from django.contrib.auth.models import User
from api.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from datetime import timedelta,datetime

import cv2
import numpy as np
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.http import JsonResponse
import base64

@login_required(login_url='/login/')
def dashboard(request):
    if request.user.is_superuser:
        allUsers=UserProfile.objects.all()
        allMessages=MessagesFor.objects.all()
        allBorders=BorderRegistration.objects.all()
        return render(request,"dashboard.html",{"allUsers":allUsers,"allMessages":allMessages,"allBorders":allBorders})
    else:
        return redirect("/border/")


@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    
    return redirect("/login/")

def loginUser(request):
    status=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
                status='Dont have permittion to this user'
                login(request,user)
                return redirect("/")
            else:
                login(request,user)
                return redirect('/border/')
        else:
            status='Usernameka ama Passwordka ayaa qaldan'
    data={
        'status':status
    }
    return render(request,"login.html",data)





def cropFaceImageToBase64(request):
    path="C:/Users/qaamuus/Documents/mohaData/landBorderP/landApp/haarcascade_frontalface_default.xml"
    img = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR) # Read the uploaded image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) # Detect faces
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        cropped = img[y:y+h, x:x+w] # Crop the image to the first detected face
        buffer = BytesIO()
        cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB) # Convert the cropped image to RGB format
        pil_image = Image.fromarray(cropped) # Convert the cropped image to a PIL Image object
        pil_image.save(buffer, format='JPEG') # Save the PIL Image to a buffer in JPEG format
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8') # Convert the buffer to a base64-encoded string
        return JsonResponse({'image_data': image_data})
    else:
        return JsonResponse({'error': 'no face detected'})


def cropFaceImage(theFullImage):
    url=theFullImage
    path="C:/Users/qaamuus/Documents/mohaData/landBorderP/landApp/haarcascade_frontalface_default.xml"
    # img = cv2.imread(url)
    img = cv2.imdecode(np.frombuffer(request.FILES['faceDetected'].read(), np.uint8), cv2.IMREAD_COLOR) # Read the uploaded image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) # Detect faces
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        cropped = img[y:y+h, x:x+w] # Crop the image to the first detected face
        buffer = BytesIO()
        cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB) # Convert the cropped image to RGB format
        pil_image = Image.fromarray(cropped) # Convert the cropped image to a PIL Image object
        pil_image.save(buffer, format='JPEG') # Save the PIL Image to a buffer in JPEG format
        image_file = InMemoryUploadedFile(buffer, None, 'image.jpg', 'image/jpeg', buffer.getbuffer().nbytes, None) # Create an InMemoryUploadedFile from the buffer
        return image_file
        # Save the UserProfile instance
    else:
        return "no face"

def validateImages(request):
    allUsers=UserProfile.objects.first()
    my_model = UserProfile.objects.first()
    
    
    

    
    return render(request,'bb.html')






# Create your views here.
# userprofile

@login_required(login_url='/login/')
def userProfileRegister(request):
    if request.user.is_superuser:
        return render(request,"user-profile/register.html")
    else:
        return redirect("/border/")
    
@login_required(login_url='/login/')
def allUserProfiles(request):
    if request.user.is_superuser:
        allUsers=UserProfile.objects.all()
        return render(request,"user-profile/list.html",{"allUsers":allUsers})
    else:
        return redirect("/border/")



def generateRandomBorderGeneratedId():
    randomNum ='borderId_'+str(BorderRegistration.objects.last().pk+1)
    return randomNum
def three_month_from_today():
    return datetime.now() + timedelta(days=60)   





# border

@login_required(login_url='/login/')
def borderRegister(request):
    # myUser=UserProfile.objects.filter(theUser=request.user).first()
    if request.user.is_superuser:
        allUsers=UserProfile.objects.all()
        theGeneratedId=generateRandomBorderGeneratedId()
        expireDate=three_month_from_today()
        return render(request,"border/register.html",{"allUsers":allUsers,"generatedUserId":theGeneratedId,"expireDate":expireDate})
    else:
        return redirect("/border/")
    


@login_required(login_url='/login/')
def allBorder(request):
    if request.user.is_superuser:
        allBorders=BorderRegistration.objects.all()
        return render(request,"border/list.html",{"allBorders":allBorders})
    else:
        return redirect("/border/")





# information
# @login_required(login_url='/login/')
def scanUserFace(request):
    # if request.user.is_superuser:
    allUsers=UserProfile.objects.all()
    return render(request,"info/scan-user-face.html",{"allUsers":allUsers})
    # else:
    #     return redirect("/border-info/")

# @login_required(login_url='/login/')
def scanedUserInfo(request,pk):
    # if request.user.is_superuser:
    userInfo = UserProfile.objects.filter(pk=pk).first()
    allBorders = BorderRegistration.objects.filter(theUser=userInfo)
    return render(request,"info/scanned-user-info.html",{"userInfo":userInfo,"allBorders":allBorders})
    # else:
    #     return redirect("/border-info/")







@login_required(login_url='/login/')
def faceDetect(request):
    return render(request,"face_detect.html")






# Qaasim_99qaasiM@99







@login_required(login_url='/login/')
def borderInfoDashboard(request):
    if request.user.is_superuser==False:
        currentUserInfo = UserProfile.objects.filter(theUser=request.user).first()
        allBorders = BorderRegistration.objects.filter(theUser=currentUserInfo)
        allMessages = MessagesFor.objects.filter(theUser=currentUserInfo)
        return render(request,"border-info-pages/border-dashboard.html",{"currentUserInfo":currentUserInfo,"allBorders":allBorders,"allMessages":allMessages})
    else:
        return redirect("/")


@login_required(login_url='/login/')
def borderInfoMessages(request):
    if request.user.is_superuser==False:
        currentUserInfo = UserProfile.objects.filter(theUser=request.user).first()
        allMessages = MessagesFor.objects.filter(theUser=currentUserInfo)
        return render(request,"border-info-pages/border-messages.html",{"allMessages":allMessages})
    else:
        return redirect("/")


# report
def messageInfo(request):
    allMessages =MessagesFor.objects.all()
    allUsers =UserProfile.objects.filter(is_superuser=False)
    return render(request,"info/message.html",{"allMessages":allMessages,"allUsers":allUsers})




# report
def reportList(request):
    allReport = ReportInfo.objects.all()
    return render(request,"report/list.html",{"allReport":allReport})


# report
def forgetPasword(request):
    if request.POST:
        username=UserProfile.objects.filter(username=request.POST.get('username'))
        password=request.POST.get('password')
        
        if username.exists():
            username=username.first()
            username.theUser.set_password(password)
            username.theUser.save()
            return render(request,"forget-password.html",{"change":"1","status":"succesfuly password changed"})
        else:
             return render(request,"forget-password.html",{"change":"2","status":"username not exit"})
    return render(request,"forget-password.html",{"change":"0","status":"username not exit"})