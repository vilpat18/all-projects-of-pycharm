from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from queryapp.models import Employee,Manager,Contact_info
from queryapp.serialisers import EmployeeSerializer,ManagerSerializer,ContactSerializer
from rest_framework.response import Response

class ContactListAOIView(APIView):
    contact = Contact_info.objects.all()
    serializer = ContactSerializer


class EmployeeListAPIView(APIView):
    def get(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data)


class ManagerListAPIView(APIView):
    def get(self,request):
        manager = Manager.objects.all()
        serializer = ManagerSerializer(manager,many=True)
        return Response(serializer.data)




