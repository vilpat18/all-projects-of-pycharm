"""Auth_Perm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from authperapp import views

router = DefaultRouter()

router.register('employee',views.EmployeeModelViewSetAPI,basename='employee')
router.register('emp1',views.EmployeeModelViewSetAPI1,basename='emp1')
router.register('emp2',views.EmployeeModelViewSetAPI2,basename='emp2')
router.register('emp3/',views.EmployeeModelViewSetAPI3,basename='emp3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
