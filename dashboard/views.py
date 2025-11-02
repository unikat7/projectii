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
    sem_user=user.semester
    courses=Courses.objects.filter(sem=user.semester).count()
    teacher=Teacher.objects.filter(user__semester=sem_user).count()
    user_data=user.profilepicture
    if user.role!="student":
        return redirect("signin")
    return render(request,"userdashboard/studentdashboard.html",{
        "user_data":user_data,
        "user":user,
        "courses":courses,
        "teacher":teacher
    })

def admindashboard(request):
    return render(request,"userdashboard/admindashboard.html")

def teachertable(request,id):

    teacher=Teacher.objects.all()
    semester=Semester.objects.get(id=id)
    courses=semester.courses.all()

    return render(request,"infotable/teachertable.html",{
        "teacher":teacher,
        "courses":courses,
        "semester":semester
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


def SemWiseTeacher(request):
    semester_number=Semester.objects.all()
    return render(request,"infotable/semesterteacher.html",{
        "semester":semester_number
    })



