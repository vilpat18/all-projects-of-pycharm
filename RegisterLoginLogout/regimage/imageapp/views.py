from django.shortcuts import render

# Create your views here.
from imageapp.serializers import RegistrationSerializer ,LoginSerializer
# from django.http import HttpResponse
from rest_framework import generics
from imageapp.models import Register ,login


class RegisterListview(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegistrationSerializer

class loginview(generics.ListCreateAPIView):
    queryset = login.objects.all()
    serializer_class = LoginSerializer
