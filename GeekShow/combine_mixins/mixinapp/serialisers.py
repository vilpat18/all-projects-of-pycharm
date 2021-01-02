from mixinapp.models import Teams

from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id','Mumbai','Delhi','Banglore']

