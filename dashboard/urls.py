from django.urls import path
from .views import teacherdashboard,studentdashboard,admindashboard,teachertable,SemesterSelection,CoursesTable


urlpatterns = [
    path("",admindashboard,name="admindash"),
    path("teacher/",teacherdashboard,name="teacherdash"),
    path("student/",studentdashboard,name="studentdash"),
    path("teachertable/",teachertable,name="teachertable"),
    path("semselection/",SemesterSelection,name="semselection"),
    path("coursestable/<int:id>",CoursesTable,name="coursestable")
]
