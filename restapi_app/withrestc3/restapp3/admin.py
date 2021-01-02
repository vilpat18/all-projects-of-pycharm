from django.contrib import admin
from restapp3.models import Players
# Register your models here.

class PlayersAdmin(admin.ModelAdmin):
    list_display = ['id','pno','pname','pruns','pteam']


admin.site.register(Players,PlayersAdmin)