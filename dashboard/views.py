from django.shortcuts import render,redirect
from .models import Teacher,Semester,Courses,Marks
from django.contrib.auth.decorators import login_required
from userprofile.models import User,ProfilePicture
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db.models import Q


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



def MarksAssign(request,id):
    students=User.objects.filter(semester=id , role='student')
    level=id
    teacher = Teacher.objects.get(user=request.user)
    course=Courses.objects.filter(teacher=teacher,sem__sem=level)

    if request.method=="POST":
        for stu in students:
            for c in course:
                    if request.method=="POST":
                        student=stu.id
                        teacher=request.user 
                        co=c.name
                        marks=request.POST.get(f"marks_{ stu.id }")
                        mark=Marks.objects.create(student=student,teacher=teacher,course=co,marks=marks)
                        mark.save()
    return render(request,"infotable/marksassign.html",{
        "students":students,
        "course":course,
        "level":level,
    })



def Result(request):
    semester_obj = Semester.objects.get(sem=request.user.semester)
    
    subject=semester_obj.courses.all()
    mark_of_student=Marks.objects.filter(student=request.user.id)
  
    print(subject)
    print(mark_of_student)
    return render(request,"infotable/result.html",{
        "courses":subject,
        "marks":mark_of_student
    })


