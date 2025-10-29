from django.urls import path
from .views import RegisterUser,signin

urlpatterns = [
    path("",RegisterUser,name="registeruser"),
    path("signin/",signin,name="signin")
]
