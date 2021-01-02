from django.contrib import admin

# Register your models here.
from.models import Place,Waiter,Restaurant

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['id','restaurant','name']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['place','serves_burger','serves_pizza']