from .models import OdiBattingRecord,BowlingRecord
from rest_framework import serializers


class OdiBattingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdiBattingRecord
        fields = ['id','name','country','runs','fifties','centuries','double_centuries']


class BowlingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BowlingRecord
        fields = ['id','name','country','wickets','five','best']