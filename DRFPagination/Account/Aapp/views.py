from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import MyAccountManager,Account
from .serialisers import MyAccountSerializer,AccountSerializer

#
# class RegistrationApiView(generics.CreateAPIView):
#     queryset = MyAccountManager.objects.all()
#     serializer_class = MyAccountSerializer


class AccountApiView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer