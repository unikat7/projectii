from django.urls import path
from .views import RegisterUser,signin,log_out,UserInfo,UpdateUserInfo

urlpatterns = [
    path("",RegisterUser,name="registeruser"),
    path("signin/",signin,name="signin"),
    path("logout/",log_out,name="logout"),
    path("userinfo/",UserInfo,name="userinfo"),
    path("updateuserinfo/",UpdateUserInfo,name="updateinfo")
]
