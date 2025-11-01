from django.db import models
from userprofile.models import User,ProfilePicture

# Create your models here.
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    profile_pic=models.OneToOneField(ProfilePicture,on_delete=models.CASCADE)

    
class Semester(models.Model):
    sem=models.IntegerField()
    def __str__(self):
        return str(self.sem)

class Courses(models.Model):
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name="courses")
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    credit_hour=models.IntegerField(default=1)


    def __str__(self):
        return self.name