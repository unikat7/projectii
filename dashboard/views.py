from django.shortcuts import render
from .models import Teacher

# Create your views here.
def teacherdashboard(request):
    return render(request,"userdashboard/teacherdashboard.html")

    
def studentdashboard(request):
    return render(request,"userdashboard/studentdashboard.html")

def admindashboard(request):
    return render(request,"userdashboard/admindashboard.html")

def teachertable(request):
    teacher=Teacher.objects.all()

    return render(request,"infotable/teachertable.html",{
        "teacher":teacher
    })