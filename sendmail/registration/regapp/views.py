from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from regapp.serializers import RegistrationSerializer

@api_view(['POST',])
def Registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data =request.data)
        data = {}
        if serializer.is_valid():
            register = serializer.save()
            data['Response'] = 'sucesfull register new user'
            data['email'] = register.email
            data['username'] = register.username
        else:
            data = serializer.errors
        return Response(data)
