from django.contrib import admin

# Register your models here.
from django.contrib import admin
from viewapp.models import Players
# Register your models here.

class PlayersAdmin(admin.ModelAdmin):
    list_display = ['id','pno','pname','pruns','pteam']


admin.site.register(Players,PlayersAdmin)