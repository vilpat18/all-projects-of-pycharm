from django.contrib import admin
from testappS.models import Student


# Register your models here.


class student_admin(admin.ModelAdmin):
    list_display = ['roll_no','name','dob','marks','email','phone','address']


admin.site.register(Student,student_admin)