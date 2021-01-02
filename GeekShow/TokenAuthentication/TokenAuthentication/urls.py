from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from tokenapp import views

router = DefaultRouter()

router.register('odi',views.OdiRecordModelViewSet,basename='odi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',obtain_auth_token)
]
