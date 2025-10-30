from django.db import models
from userprofile.models import User,ProfilePicture

# Create your models here.
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    profile_pic=models.OneToOneField(ProfilePicture,on_delete=models.CASCADE)

    

