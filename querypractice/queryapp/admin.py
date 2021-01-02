from django.contrib import admin

# Register your models here.

from queryapp.models import Employee,Manager,Contact_info

admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Contact_info)
