from django.contrib import admin
from django.urls import path
from testapp5 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view)
]
