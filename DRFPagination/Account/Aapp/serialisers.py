from .models import MyAccountManager,Account
from rest_framework import serializers


class MyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAccountManager
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'