from django.shortcuts import render

# Create your views here.
def teacherdashboard(request):
    return render(request,"userdashboard/teacherdashboard.html")

    
def studentdashboard(request):
    return render(request,"userdashboard/studentdashboard.html")

def admindashboard(request):
    return render(request,"userdashboard/admindashboard.html")