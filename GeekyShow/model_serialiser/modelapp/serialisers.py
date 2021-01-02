from rest_framework import serializers
from modelapp.models import Student


class StudentSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']