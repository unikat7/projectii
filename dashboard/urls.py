from django.urls import path
from .views import teacherdashboard,studentdashboard,admindashboard,teachertable,SemesterSelection,CoursesTable,SemWiseTeacher


urlpatterns = [
    path("",admindashboard,name="admindash"),
    path("teacher/",teacherdashboard,name="teacherdash"),
    path("student/",studentdashboard,name="studentdash"),
    path("teachertable/<int:id>",teachertable,name="teachertable"),
    path("semselection/",SemesterSelection,name="semselection"),
    path("coursestable/<int:id>",CoursesTable,name="coursestable"),
    path("semteacher/",SemWiseTeacher,name="semwiseteacher")
]
