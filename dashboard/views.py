from django.shortcuts import render,redirect
from .models import Teacher,Semester,Courses
from django.contrib.auth.decorators import login_required
from userprofile.models import User,ProfilePicture
from django.contrib.auth import logout


# Create your views here.
def teacherdashboard(request):
    return render(request,"userdashboard/teacherdashboard.html")

@login_required(login_url='signin')
def studentdashboard(request):
  
    user=request.user
    courses=Courses.objects.filter(sem=user.semester).count()
    user_data=user.profilepicture
    if user.role!="student":
        return redirect("signin")
    return render(request,"userdashboard/studentdashboard.html",{
        "user_data":user_data,
        "user":user,
        "courses":courses
    })

def admindashboard(request):
    return render(request,"userdashboard/admindashboard.html")

def teachertable(request):
    teacher=Teacher.objects.all()

    return render(request,"infotable/teachertable.html",{
        "teacher":teacher
    })

def SemesterSelection(request):
    sem=Semester.objects.all()
    return render(request,"infotable/semesterselection.html",{
        "sem":sem
    })



def CoursesTable(request,id):
    semester=Semester.objects.get(id=id)
    sem_data=semester.courses.all()
    return render(request,"infotable/coursestable.html",{
        "sem_data":sem_data,
        "semester":semester
    }
    )


