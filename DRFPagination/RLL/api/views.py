from django.shortcuts import render

from rest_framework import generics,permissions
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        global user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
        return Response({"user":UserSerializer(context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1]})

