from agentapp.models import GetQuate
from rest_framework import serializers

class GetQouteSerialiser(serializers.ModelSerializer):
    objects = None

    class Meta:
        model = GetQuate
        fields = ['zip_code','select_type']










