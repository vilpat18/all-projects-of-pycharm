from django.contrib import admin
from jobapp.models import PythonStudent
from jobapp.models import Contacts
from jobapp.models import About
from jobapp.models import Courses



# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','mob','email','totalfees','paid','due']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['Gmail','Linkdin','Yahoo','landline','mobile','mobile2']

class AboutusAdmin(admin.ModelAdmin):
    list_display = ['info']

class CouseAdmin(admin.ModelAdmin):
    list_display = ['python','sap','matlab','dba','plsql','rpa','salesforce']


admin.site.register(Contacts,ContactAdmin),
admin.site.register(PythonStudent,StudentAdmin),
admin.site.register(About,AboutusAdmin),
admin.site.register(Courses,CouseAdmin)











