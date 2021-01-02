from .models import User,CUser,Employee
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']


class CUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = ('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','username','first_name','last_name','email','salary']
