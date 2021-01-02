
from django.contrib import admin
from django.urls import path,include
from viewsetapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('OdiRecord',views.OdiRecordViewSet,basename='OdiRecord')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
