from django.contrib import admin

# Register your models here.
from .models import Employee,Person
from import_export.admin import ImportExportModelAdmin

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
# list_display = ['id','name','email','birth_date','location']