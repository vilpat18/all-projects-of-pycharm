from django.shortcuts import render

# Create your views here.

# from rest_framework.response import Response
from rgapp.serializers import RegistrationSerializer ,LoginSerializer
# from django.http import HttpResponse
from rest_framework import generics
from rgapp.models import Register ,login


class RegisterListview(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegistrationSerializer

class loginview(generics.ListCreateAPIView):
    queryset = login.objects.all()
    serializer_class = LoginSerializer


# def register_view(request):
# if request.method == 'POST':
#     serializer =RegistrationSerializer(data = request.data)
#     data = {}
#     if serializer.is_valid():
#         register = serializer.save()
#         data['HttpResponse'] = 'successful register new user '
#         data['first_name'] = register.first_name
#         data['last_name'] = register.last_name
#         data['email'] = register.email
#         data['mobile'] = register.mobile
#         data['password'] = register.password
#         data['confirm_password'] = register.confirm_password
#         data['recovery_email'] = register.recovery_email
#     else :
#         data = serializer.errors
#     return HttpResponse(data)
#


