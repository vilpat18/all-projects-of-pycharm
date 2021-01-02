"""generic_mixin_API URL Configuration

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
from django.urls import path
from gemixapp import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API documentaion')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_document',schema_view),
    path('api/stu/',views.StudentListModelMixinAPI.as_view()),
    path('api/stu/post/',views.StudentCreateModelMixinAPI.as_view()),
    path('api/stu/<int:pk>/',views.StudentRetrieveModelMixinAPI.as_view()),
    path('api/stu/put/<int:pk>',views.StudentUpdateModelMixinAPI.as_view()),
    path('api/stu/del/<int:pk>',views.StudentDestroyModelMixinAPI.as_view()),
]
