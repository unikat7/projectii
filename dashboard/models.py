from django.db import models
from userprofile.models import User,ProfilePicture

# Create your models here.
class Semester(models.Model):
    sem=models.IntegerField()
    def __str__(self):
        return str(self.sem)

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.OneToOneField(ProfilePicture,on_delete=models.CASCADE)
    semester=models.ManyToManyField(Semester,blank=True)


    def __str__(self):
        return self.user.username

class Courses(models.Model):
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name="courses")
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,default=True,related_name='teacher')
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    credit_hour=models.IntegerField(default=1)


    def __str__(self):
        return self.name



class Marks(models.Model):
    # student=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role': 'student'},related_name="student_mark")
    student=models.IntegerField()
    teacher=models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'},related_name="teacher_mark")
    course=models.CharField(max_length=200,blank=True,null=True)
    marks=models.FloatField()


    def __str__(self):
        return self.course


    




