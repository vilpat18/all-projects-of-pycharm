from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view , authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serialisers import StudentSerialiser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialiser(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerialiser(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerialiser(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerialiser(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted successfully'})












