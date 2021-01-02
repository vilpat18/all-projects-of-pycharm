from django.shortcuts import render

# Create your views here.
from .models import Employee
from .serialisers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .custompermissions import MyPermission


class EmployeeModelViewSetAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [BasicAuthentication,]
    # permission_classes = [IsAuthenticated,]


class EmployeeModelViewSetAPI1(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class EmployeeModelViewSetAPI2(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class EmployeeModelViewSetAPI3(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [MyPermission,]

