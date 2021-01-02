from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from .models import OdiBattingRecord
from .serialisers import OdiBattingRecordSerializer
from rest_framework import status
from rest_framework import viewsets


class OdiRecordViewSet(viewsets.ViewSet):
    def list(self,request):
        odi = OdiBattingRecord.objects.all()
        serializer = OdiBattingRecordSerializer(odi,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            odi = OdiBattingRecord.objects.get(id=id)
            serializer = OdiBattingRecordSerializer(odi)
            return Response(serializer.data)

    def create(self,request):
        serializer = OdiBattingRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def update(self,request,pk=None):
        id = pk
        if id is not None:
            odi = OdiBattingRecord.objects.get(id=id)
            serializer = OdiBattingRecordSerializer(odi)
            return Response(serializer.data)

    def partial_update(self,request,pk=None):
        id = pk
        odi = OdiBattingRecord.objects.get(id=id)
        serializer = OdiBattingRecordSerializer(odi,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def destroy(self,request,pk=None):
        odi = OdiBattingRecord.objects.get(id=id)
        odi.delete()
        return Response('data deleted successfully')

