from rest_framework import serializers

class NameSerializer(serializers.serializer):
    name = serializers.CharField(max_length=20)
