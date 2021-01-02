from django.shortcuts import render

# Create your views here.

from regapp.serialisers import RegisterSerializer,LoginSerializer,ChangePasswordSerializer
from rest_framework import generics
from regapp.models import Login,Register
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class RegisterListView(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class LoginListView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ChangePasswordView(generics.UpdateAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)


    def get_object(self,queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('password')):
                return Response({'password':['wrong password']},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status':'success',
                'code':status.HTTP_200_OK,
                'message':'password update successfully',
                'data':[]
            }

            return Response(response)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
