from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    role_choices=(
        ('admin','admin'),
        ('teacher','teacher'),
        ('student','student')
    )

    role=models.CharField(max_length=10,choices=role_choices)
    semester=models.IntegerField(default=1)


    def __str__(self):
        return self.username

class ProfilePicture(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.user.username








