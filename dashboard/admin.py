from django.contrib import admin
from .models import Teacher,Semester,Courses

# Register your models here.

admin.site.register([Teacher,Semester,Courses])
