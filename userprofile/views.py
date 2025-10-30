from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import re
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def RegisterUser(request):

    if request.method=='POST':
        data=request.POST
        firstname=data['firstname']
        lastname=data['lastname']
        username=data['username']
        password=data['password']
        semester=data['semester']
        email=data['email']
        role=data['role']
        errors=[]
        if User.objects.filter(username=username):
                 errors.append("Username already exists")
          
            
        pass_regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        if not re.match(pass_regex, password):
            errors.append("Password must have uppercase, lowercase, number, special character, and at least 8 characters")
        if errors:
            for err in errors:
                messages.error(request, err)
            return render(request,"profile/register.html")

        user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email,role=role,semester=semester)
        if user is not None:
            user.save()
        
    return render(request,"profile/register.html")


def signin(request):
    if request.method=="POST":
        data=request.POST
        username=data["username"]
        password=data["password"]
        role=data["role"].lower()
        semester=data["semester"]
        user=authenticate(username=username,password=password,role=role,semester=semester)
        if user is not None:
            if user.role=='teacher':
                return redirect('teacherdash')
            if user.role=='student':
                return redirect("studentdash")
            if user.role=='amdin':
                return redirect('admindash')
        else:
            messages.error(request,"invalid credentials")
            return redirect('signin')

    return render(request,"profile/login.html")


