from django.shortcuts import render
from django.contrib.auth.models import User
from landApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Create your views here.
# @login_required(login_url='/login/')
def dashboard(request):
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


def face(request):
    return render(request,"face.html")
