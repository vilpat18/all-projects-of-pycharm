from django.shortcuts import render

# Create your views here.
from rest_framework import status

from OneToOne.serialisers import PageSerialiser, CreatorSerialiser
from rest_framework.views import APIView
from OneToOne.models import Creator, Page
from rest_framework.response import Response

class Creatorlist(APIView):
    def get(self, request, format=None):
        creator = Creator.objects.all()
        serialiser = CreatorSerialiser(creator, many=True)
        return Response(serialiser.data)

    def post(self, request, format=None):
        serializer = PageSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)