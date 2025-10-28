from django.shortcuts import render
from .models import User
from django.contrib import messages



# Create your views here.


def RegisterUser(request):
    error=[]
    if request.method=='POST':
        data=request.POST
        firstname=data['firstname']
        lastname=data['lastname']
        username=data['username']
        password=data['password']
        email=data['email']
        role=data['role']
        if User.objects.filter(username=username):
            messages.error(request,"username already exist")
          
            
        pass_regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        if password not in pass_regex:
            messages.error(request,"please put strong password")
          
        user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email,role=role)
        if user is not None:
            user.save()
        
    return render(request,"register.html")

    