from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from agentapp.serializers import GetQouteSerialiser
from agentapp.models import GetQuate

class getqouteview(generics.ListCreateAPIView):
    serializer_class = GetQouteSerialiser
    def get_queryset(self):
        getqoute = GetQouteSerialiser.objects.all()
        return getqoute

