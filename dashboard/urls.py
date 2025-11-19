from django.urls import path
from .views import Teacherdashboard,studentdashboard,teachertable,SemesterSelection,CoursesTable,SemWiseTeacher,DeleteCourse,AddTeacher,MarksAssign,Result,Change_Password,PassChangeSuccess,TechInquiry,StudentView

urlpatterns = [
    path("teacher/",Teacherdashboard,name="teacherdash"),
    path("student/",studentdashboard,name="studentdash"),
    path("teachertable/<int:id>",teachertable,name="teachertable"),
    path("semselection/",SemesterSelection,name="semselection"),
    path("coursestable/<int:id>",CoursesTable,name="coursestable"),
    path("semteacher/",SemWiseTeacher,name="semwiseteacher"),
    path("deletecourse/<int:id>",DeleteCourse,name="deletecourse"),
    path("addteacher/",AddTeacher,name="addteacher"),
    path("markassign/<int:id>",MarksAssign,name="markassign"),
    path("result/",Result,name="result"),
    path('change-password/', Change_Password, name='change_password'),
    path('successpass/',PassChangeSuccess,name="successpass"),
    #ml model 
    path('tech/',TechInquiry,name='tech'),
    #student view
    path('viewstudent/',StudentView,name="viewstudent")
]






