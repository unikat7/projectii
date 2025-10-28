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


    def __str__(self):
        return self.username







