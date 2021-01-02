from MVSApp.models import OdiBattingRecord
from rest_framework import serializers


class OdiBattingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdiBattingRecord
        fields = ['id','name','country','runs','fifties','centuries','double_centuries']