from django.contrib import admin

# Register your models here.
from MVSApp.models import OdiBattingRecord


@admin.register(OdiBattingRecord)
class OdiBattingRecordAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','runs','fifties','centuries','double_centuries']