from django.contrib import admin

# Register your models here.
from classapp.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','marks','city']

