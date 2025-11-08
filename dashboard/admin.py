from django.contrib import admin
from .models import Teacher,Semester,Courses,Marks

# Register your models here.

admin.site.register([Teacher,Semester,Courses,Marks])
