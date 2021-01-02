from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from dataapp.serializers import EmployeeSerializer, DepartmentsSerializer,\
    DeptManagerSerializer, DeptEmpSerializer, SalariesSerializer, TitlesSerializers

from dataapp.models import Employees, Departments, DeptManager, DeptEmp, Salaries, Titles
from rest_framework.authentication import TokenAuthentication
from dataapp.permissions import IsReadOnly ,AllPermission
class EmployeeAPI(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]

class DepartmentsAPI(ModelViewSet):
    serializer_class = DepartmentsSerializer
    queryset = Departments.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]

class DeptManagerAPI(ModelViewSet):
    serializer_class = DeptManagerSerializer
    queryset = DeptManager.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllPermission]


class DeptEmpAPI(ModelViewSet):
    serializer_class = DeptEmpSerializer
    queryset = DeptEmp.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]

class SalariesAPI(ModelViewSet):
    serializer_class = SalariesSerializer
    queryset = Salaries.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]

class TitlesAPI(ModelViewSet):
    serializer_class = TitlesSerializers
    queryset = Titles.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]