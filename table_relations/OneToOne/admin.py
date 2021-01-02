from django.contrib import admin

# Register your models here.
from OneToOne.models import Creator,Page

admin.site.register(Creator)

admin.site.register(Page)