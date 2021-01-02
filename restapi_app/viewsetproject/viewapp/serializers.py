from viewapp.models import Players
from rest_framework.serializers import ModelSerializer

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'
