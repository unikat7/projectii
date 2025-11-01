from django.urls import path
from .views import RegisterUser,signin,log_out

urlpatterns = [
    path("",RegisterUser,name="registeruser"),
    path("signin/",signin,name="signin"),
    path("logout/",log_out,name="logout")
]
