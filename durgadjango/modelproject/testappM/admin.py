from django.contrib import admin
from testappM.models import Employee



# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['e_no','e_name','e_salary','e_add']






admin.site.register(Employee,EmployeeAdmin)
