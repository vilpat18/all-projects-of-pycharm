from django.contrib import admin

# Register your models here.
from .models import User,CUser,Employee

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']

@admin.register(CUser)
class CUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']


@admin.register(Employee)
class CUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email','salary']