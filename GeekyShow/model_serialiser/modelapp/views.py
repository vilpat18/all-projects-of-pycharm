from django.shortcuts import render
from modelapp.models import Student
from modelapp.serialisers import StudentSerialisers
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class StudentListCreateAPIView(APIView):
    def get(self,request):
        student = Student.objects.all()
        serialiser = StudentSerialisers(student,many=True)
        return Response(serialiser.data)

    def post(self,request):
        serialiser = StudentSerialisers(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
        return Response(serialiser.data)

    def update(self,request):
        serialiser = StudentSerialisers(data=request.data,partial_update=True)
        if serialiser.is_valid():
            serialiser.save()
        return Response(serialiser.data)
