from rest_framework import serializers
from REST_API.models import Teachers

class StudentSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=100)
    l_name = serializers.CharField(max_length=100)
    roll_number = serializers.IntegerField()


class TeacherSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=100)

def create(self,validate_data):
    return Teachers.objects.create(**validate_data)

