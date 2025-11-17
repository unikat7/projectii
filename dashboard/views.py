from django.shortcuts import render,redirect
from .models import Teacher,Semester,Courses,Marks
from django.contrib.auth.decorators import login_required
from userprofile.models import User,ProfilePicture
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
#model setup

import os
import pandas as pd
import joblib
from django.conf import settings


ML_FOLDER = os.path.join(settings.BASE_DIR, 'dashboard', 'ml_model') 
model = joblib.load(os.path.join(ML_FOLDER, 'tech_path_model.pkl'))
train_columns = joblib.load(os.path.join(ML_FOLDER, 'train_columns.pkl'))


# Create your views here.
def teacherdashboard(request):
    return render(request,"userdashboard/teacherdashboard.html")

@login_required(login_url='signin')
def studentdashboard(request):
  
    user=request.user
    sem_user=user.semester
    courses=Courses.objects.filter(sem=user.semester).count()
 

    if user.role!="student":
        return redirect("signin")
    return render(request,"userdashboard/studentdashboard.html",{
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
    action=request.GET.get("action")

    sem=Semester.objects.all()

    return render(request,"infotable/semesterselection.html",{
        "sem":sem,
        "action":action
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

    if request.user.role=='teacher':
        student_count=User.objects.filter(role='student').count()
        return render(request,"userdashboard/teacherdashboard.html",{
            "student_count":student_count,
       
        })
    else:
        return HttpResponse("u r not allowed here ")


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
                        if(Marks.objects.filter(student=student,course=co)).exists():
                            messages.error(request,"the mark is already assigned to the student")
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
    mark_count=mark_of_student.count()
  
    print(subject)
    print(mark_of_student)
    return render(request,"infotable/result.html",{
        "courses":subject,
        "marks":mark_of_student,
        "mark_count":mark_count
    })

@login_required(login_url='signin')
def Change_Password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=="POST":
        data=request.POST
        form=PasswordChangeForm(user=request.user,data=data)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            return redirect("successpass")
    return render(request,"password/changepassword.html",{
        "form":form
    })

@login_required(login_url='signin')
def PassChangeSuccess(request):
    return render(request,"password/success.html")



#giving the data to the model to predict the path 
def TechInquiry(request):
    prediction = None 

    if request.method == 'POST':
        data = request.POST

   
        user_input = {
            'prefer_design_or_logic': data['prefer_design_or_logic'],
            'like_coding': data['like_coding'],
            'enjoy_math': data['enjoy_math'],
            'like_puzzles': data['like_puzzles'],
            'build_apps_or_websites': data['build_apps_or_websites']
        }

      
        user_df = pd.DataFrame([user_input])

        # One-hot encode categorical features
        user_df = pd.get_dummies(user_df, columns=[
            'prefer_design_or_logic', 'like_coding', 'enjoy_math', 'like_puzzles', 'build_apps_or_websites'
        ])

        for col in train_columns:
            if col not in user_df.columns:
                user_df[col] = 0

        user_df = user_df[train_columns]

        prediction = model.predict(user_df)[0]

    return render(request, "techpath/techform.html", {"prediction": prediction})


