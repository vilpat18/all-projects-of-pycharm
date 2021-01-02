from django.contrib import admin

# Register your models here.
from .models import Article,Reporter

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline','pub_date','reporter']