from django.contrib import admin

# Register your models here.
from regapp.models import Student, StudentInfo

admin.site.register(Student)
admin.site.register(StudentInfo)