from django.contrib import admin
from studentapp.models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollnumber','name','dob','marks','email','phone','address']





admin.site.register(Student,StudentAdmin)
