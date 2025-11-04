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
    student_count=User.objects.filter(role='student').count()
    teacher_count=User.objects.filter(role='teacher').count()
    courses_count=Courses.objects.all().count()
    return render(request,"userdashboard/admindashboard.html",{
        "student_count":student_count,
        "teacher_count":teacher_count,
        "courses_count":courses_count
    })

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



@login_required(login_url='signin')
def Teacherdashboard(request):
    student_count=User.objects.filter(role='student').count()
    return render(request,"userdashboard/teacherdashboard.html",{
        "student_count":student_count
    })


def DeleteCourse(request,id):
    course=Courses.objects.get(id=id)
    course.delete()
    return redirect("coursestable")


def AddTeacher(request):
    user=User.objects.all()
    
    return render(request,"addteacher.html",{
        "user":user
    })




