from django.urls import path
from .views import Teacherdashboard,studentdashboard,admindashboard,teachertable,SemesterSelection,CoursesTable,SemWiseTeacher,DeleteCourse,AddTeacher


urlpatterns = [
    path("",admindashboard,name="admindash"),
    path("teacher/",Teacherdashboard,name="teacherdash"),
    path("student/",studentdashboard,name="studentdash"),
    path("teachertable/<int:id>",teachertable,name="teachertable"),
    path("semselection/",SemesterSelection,name="semselection"),
    path("coursestable/<int:id>",CoursesTable,name="coursestable"),
    path("semteacher/",SemWiseTeacher,name="semwiseteacher"),
    path("deletecourse/<int:id>",DeleteCourse,name="deletecourse"),
    path("addteacher/",AddTeacher,name="addteacher")

]
