from django.db import models
from django_rest_framework import serializers
from user_profile.models import UserProfile

# Create your models here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
