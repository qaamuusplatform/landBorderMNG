from django.shortcuts import render
from django.contrib.auth.models import User
from landApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/login/')



@login_required(login_url='/login/')
def dashboard(request):
    try:
        currentUser=UserProfile.objects.filter(user=request.user.id).last()
        borderLevel=BorderRegistration.objects.filter(theUser=currentUser)
        allMessages=MessagesFor.objects.filter(theUser=currentUser)
        return render(request,"dashboard.html",{"messages":allMessages,"currentUser":currentUser,"borderLevel":borderLevel})
    except:
        return render(request,"dashboard.html",{"messages":{},"currentUser":{}})

def loginTheBorder(request):
    status=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
                status='Dont have permittion to this user'
            else:
                login(request,user)
                return redirect('/border/')
        else:
            status='Usernameka ama Passwordka ayaa qaldan'
    data={
        'status':status
    }
    return render(request,"login.html",data)

@login_required(login_url='/login/')
def borderInfo(request):
    try:
        currentUser=UserProfile.objects.filter(user=request.user.id).last()
        borderLevel=BorderRegistration.objects.filter(theUser=currentUser)
        return render(request,"borderInfo.html",{"borderLevel":borderLevel,"currentUser":currentUser})
    except:
        return render(request,"borderInfo.html",{"messages":{},"currentUser":{}})

@login_required(login_url='/login/')
def borderMessage(request):
    try:
        currentUser=UserProfile.objects.filter(user=request.user.id).last()
        allMessages=MessagesFor.objects.filter(theUser=currentUser)
        
        return render(request,"messages.html",{"messages":allMessages,"currentUser":currentUser})
    except:
        
        return render(request,"messages.html",{"messages":{},"currentUser":{}})
    

@login_required(login_url='/login/')
def report(request):
    try:
        currentUser=UserProfile.objects.filter(user=request.user.id).last()
        allMessages=MessagesFor.objects.filter(theUser=currentUser)
        return render(request,"report.html",{"messages":allMessages,"currentUser":currentUser})
    except:
        
        return render(request,"report.html",{"messages":{},"currentUser":{}})