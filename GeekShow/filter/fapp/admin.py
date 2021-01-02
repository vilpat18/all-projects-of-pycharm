from django.contrib import admin

# Register your models here.
from .models import OdiBattingRecord,BowlingRecord

@admin.register(OdiBattingRecord)
class OdiRecordAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','runs','fifties','centuries','double_centuries']


@admin.register(BowlingRecord)
class BowlingAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','wickets','five','best']