from django.contrib import admin


from django.contrib import admin
from dataapp.models import Employees,Departments,DeptEmp,DeptManager,Salaries,Titles
# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(DeptManager)
admin.site.register(Salaries)
admin.site.register(Titles)