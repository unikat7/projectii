from django.urls import path
from .views import teacherdashboard,studentdashboard,admindashboard,teachertable


urlpatterns = [
    path("",admindashboard,name="admindash"),
    path("teacher/",teacherdashboard,name="teacherdash"),
    path("student/",studentdashboard,name="studentdash"),
    path("teachertable/",teachertable,name="teachertable"),
]
