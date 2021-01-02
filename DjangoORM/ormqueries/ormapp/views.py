from django.db.models import query
from django.shortcuts import render
from django.db.models import Q,F,Count,Avg,Max,Min,Sum

# Create your views here.
from .models import User,CUser,Employee
from .serializers import UserSerializer,CUserSerializer,EmployeeSerializer
from rest_framework import viewsets


class UserAPIView(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # queryset = User.objects.filter(first_name__startswith='v')|User.objects.filter(last_name__startswith='n')
    # queryset = User.objects.filter(first_name__startswith='s')& User.objects.filter(last_name__startswith='p')
    # queryset = User.objects.filter(~Q(id__lt=5)) # Records beyond 5
    # queryset = User.objects.filter(~Q(id__gte=5))  # Records up to 5
    # q1 = User.objects.filter(id__gte=9)
    # q2 = CUser.objects.filter(id__gte=9)
    # queryset = q1.union(q2)
    # queryset = User.objects.filter(first_name__startswith='V').values('first_name', 'last_name')
    # queryset = User.objects.filter(username__startswith='V').only("first_name","last_name")
    # queryset = User.objects.filter(first_name=F("username")) # Find first_name similar to username
    # queryset = User.objects.filter(Q(first_name__startswith='V')& Q(last_name__startswith='P'))
    # queryset = User.objects.all().aggregate(Avg('id'))
    # queryset = User.objects.all().aggregate(Max('id'))
    serializer_class = UserSerializer

class CUserAPIView(viewsets.ModelViewSet):
    queryset = CUser.objects.all()
    serializer_class = CUserSerializer


class EmployeeAPIView(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    # queryset = Employee.objects.all().order_by('-salary')
    # second_largest = queryset[2].first_name  # Second Largest
    queryset = Employee.objects.all().aggregate(Avg('id'))


    serializer_class = EmployeeSerializer


