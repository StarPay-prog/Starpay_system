from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Login__(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'login.html')

@login_required(login_url='/Users/login/')
def Logout(request):
    logout(request)
    return redirect('/')

def Signup(request):
    if request.method == "POST":
        f_name = request.POST.get('fName')
        l_name = request.POST.get('lName')
        mobile = request.POST.get('mobile_no')
        email = request.POST.get('Email')
        password1 = request.POST.get('password1')

        print(f_name, l_name, mobile, email, password1)
        

        u = CustomUser.objects.create_user(
            contact_no=mobile, password=password1, email=email, first_name=f_name,  is_active=True, )
        u.save()
        print(type(u))
        print(u)
        
        return redirect("/Users/login/")
    else:
        print('get')
        return render(request, 'signup.html')

def Forgot_Password(request):

    
    return render(request, 'forgot-password.html')

@login_required(login_url='/Users/login/')
def Reset_Password(request):

        user = request.user
        if request.method == "POST":
            
            current = request.POST.get('present')
            password1 = request.POST.get('new')
            password2 = request.POST.get('confirm')

            if user.check_password(current):
            # Password is correct
                if password1 == password2:
                    user = CustomUser.objects.get(email=user)
                    user.set_password(password1)
                    user.save()
                    return redirect("/Users/login/")
                else:
                    return HttpResponse("Password Not Matched")
                print("Password is correct!")
            else:
            # Password is incorrect
                print("Password is incorrect.")
                return HttpResponse("Password is incorrect.")
        else:
            return render(request, 'password-change.html')

@login_required(login_url='/Users/login/')
def transections(request):

    user = request.user.email

    transections = Transection.objects.filter(From=user)
    
    context = {
        'transections':transections
    }
    return render(request, 'transaction.html', context)

@login_required(login_url='/Users/login/')
def personal(request):

    user = request.user
    print(user)
    user = CustomUser.objects.get(email=user)
    context = {
        'user':user
    }
    return render(request, 'personal.html', context)