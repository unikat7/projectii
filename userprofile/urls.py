from django.urls import path
from .views import RegisterUser

urlpatterns = [
    path("",RegisterUser,name="registeruser")
]
