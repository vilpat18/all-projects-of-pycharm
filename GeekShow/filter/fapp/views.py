from django.shortcuts import render

# Create your views here.

from .models import OdiBattingRecord,BowlingRecord
from .serialisers import OdiBattingRecordSerializer,BowlingRecordSerializer
from rest_framework.generics import ListAPIView


class BatRecordAPI(ListAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

class BowlRecordAPI(ListAPIView):
    queryset = BowlingRecord.objects.all()
    serializer_class = BowlingRecordSerializer
