from django.contrib import admin

# Register your models here.
from .models import Article,Publication

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline']


@admin.register(Publication)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['title']