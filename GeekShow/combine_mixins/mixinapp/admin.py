from django.contrib import admin

# Register your models here.

from mixinapp.models import Teams

@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','Mumbai','Delhi','Banglore']
