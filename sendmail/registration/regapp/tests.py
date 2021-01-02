from django.test import TestCase

# Create your tests here.
# from django.contrib.auth.models import User
#  from rest_framework.views import APIView
#  from rest_framework import status
#
#  class Register(APIView):
#     def post(self, request):
#       user = User.objects.create(
#                 username=request.data.get('email'),
#                 email=request.data.get('email'),
#                 first_name=request.data.get('firstName'),
#                 last_name=request.data.get('lastName')
#             )
#      user.set_password(str(request.data.get('password')))
#      user.save()
#      return Response({"status":"success","response":"User Successfully Created"}, status=status.HTTP_201_CREATED)