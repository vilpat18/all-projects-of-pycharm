from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter
from tokenapp import views

router = DefaultRouter()

router.register('odi',views.OdiRecordModelViewSet,basename='odi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_token/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('verify/',TokenVerifyView.as_view())
]
